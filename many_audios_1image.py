import os

image_source = "audio-video/images/wallhaven-d6y12l.jpg"
audio_input_dir = "audio-video/audio"
video_output = "audio-video/output/output_video.mp4"

audio_source = ""
audio_index = ""
index = 0
for file in os.listdir(audio_input_dir):
    audio_source += f'-i "{audio_input_dir}/{file}" '
    audio_index += f"[{index + 1}:0]"
    index += 1

quality = "veryfast"
fps = 30
vbr = 1000
abr = 128

command = f'-re -loop 1 -i "{image_source}" {audio_source}-filter_complex\
 "[0:v]scale=1280:720[v];{audio_index}concat=n={index}:v=0:a=1[outa]"\
 -map "[v]" -map "[outa]"\
 -c:v libx264 -preset {quality} -b:v {vbr}k -maxrate {vbr}k\
 -bufsize 2000k -pix_fmt yuv420p -r {fps} -g {fps*2} -keyint_min {fps*2}\
 -c:a aac -b:a {abr}k\
 "{video_output}"'

print(command)
os.system(command)
