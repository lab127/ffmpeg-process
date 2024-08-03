import os
from random import shuffle, randint
from time import time

start = time()


def random_playlist(lst, n):
    shuffle(lst)
    if len(lst) > n:
        # https://stackoverflow.com/a/2136090
        chunks = [lst[i::n] for i in range(n)]
        chunk_lst = chunks[randint(0, n - 1)]
        shuffle(chunk_lst)
        return chunk_lst
    return lst


image_source = "audio-video/images/kid-coffeee-by-cromaconceptovisual.jpg"
audio_folder = "audio-video/songs"
file_name = "audio-video/output/one-img-playlist-720"
video_output = "{file_name}.mp4"

lst = os.listdir(audio_folder)
playlist = random_playlist(lst, 4)

audio_source = ""
audio_index = ""
index = 0

for file in playlist:
    audio_source += f'-i "{audio_folder}/{file}" '
    audio_index += f"[{index + 1}:0]"
    index += 1

with open(f"{file_name}.txt", "w", encoding="utf-8") as fp:
    for item in playlist:
        # write each item on a new line
        fp.write("%s\n" % item.replace(".mp3", ""))
    print("Done")

# ok -
command = f'-loop 1 -i {image_source} {audio_source}-filter_complex\
 "[0:v]scale=1280:720[v];{audio_index}concat=n={index}:v=0:a=1[outa]"\
 -map "[v]" -map "[outa]"\
 -tune stillimage -pix_fmt yuv420p -shortest "{video_output}"'

print(command)
os.system(f"ffmpeg {command}")
end = time()
print(f"{len(playlist)} songs in {(end-start)}s")
