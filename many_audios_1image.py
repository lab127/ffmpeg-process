import os
from random import shuffle, randint


image_source = "audio-video/images/kid-coffeee-by-cromaconceptovisual.jpg"
audio_input_dir = "audio-video/songs"
video_output = "audio-video/output/output_video.mp4"


def random_playlist(lst, n):
    shuffle(lst)
    if len(lst > n):
        # https://stackoverflow.com/a/2136090
        chunks = [lst[i::n] for i in range(n)]
        chunk_lst = chunks[randint(0, n - 1)]
        shuffle(chunk_lst)
        return chunk_lst
    return lst


lst = os.listdir("audio-video/songs")
playlist = random_playlist(lst, 5)

audio_source = ""
audio_index = ""
index = 0
for file in playlist:
    audio_source += f'-i "{audio_input_dir}/{file}" '
    audio_index += f"[{index + 1}:0]"
    index += 1

quality = "veryfast"
fps = 24
vbr = 1000
abr = 128

command = f'-loop 1 -i "{image_source}" {audio_source}-filter_complex\
 "[0:v]scale=1280:720[v];{audio_index}concat=n={index}:v=0:a=1[outa]"\
 -map "[v]" -map "[outa]"\
 -c:v libx264 -preset {quality} -b:v {vbr}k -maxrate {vbr}k\
 -bufsize 2000k -pix_fmt yuv420p -r {fps} -g {fps*2} -keyint_min {fps*2}\
 -c:a aac -b:a {abr}k\
 "{video_output}"'

print(command)
# os.system(f"ffmpeg {command}")
