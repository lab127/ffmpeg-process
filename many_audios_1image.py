import os

image_source = "audio-video/images/wallhaven-d6y12l.jpg"
audio_input_dir = "audio-video/audio"
video_output = "audio-video/output/output_video.mp4"

audio_source = ""
audio_index = ""
audio_filter = ""
audio_map = ""
index = 0
for file in os.listdir(audio_input_dir):
    audio_source += f'-i "{audio_input_dir}/{file}" '
    audio_index += f"[{index + 1}:0]"
    index += 1
    audio_map += f"-map {index} "
    audio_filter += f"[{index}:a]atrim=end=2,asetpts=PTS-STARTPTS[a{index}];"

# ok - tinggal dikecilin
command = f'ffmpeg -r 24 -loop 1 -i "{image_source}" {audio_source}-filter_complex "{audio_index}concat=n={index}:v=0:a=1[outa]" -map 0:v -map "[outa]" -tune stillimage -pix_fmt yuv420p -shortest {video_output}'

print(command)
os.system(command)
