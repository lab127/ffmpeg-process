import os

video_source = "image.png"
audio_folder = "audio"

audio_source = ""
audio_index = ""
audio_filter = ""
audio_map = ""
index = 0
for file in os.listdir(audio_folder):
    audio_source += f'-i "{audio_folder}/{file}" '
    audio_index += f"[{index + 1}:0]"
    index += 1
    audio_map += f"-map {index} "
    audio_filter += f"[{index}:a]atrim=end=2,asetpts=PTS-STARTPTS[a{index}];"

# ok - tinggal dikecilin
command = f'ffmpeg -loop 1 -i {video_source} {audio_source}-filter_complex "{audio_index}concat=n={index}:v=0:a=1[outa]" -map 0:v -map "[outa]" -tune stillimage -pix_fmt yuv420p -shortest outputVid.mp4'

print(command)
os.system(command)
