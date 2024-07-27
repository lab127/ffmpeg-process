import os

video_dir = "folder2"
yt_url = "rtmp://a.rtmp.youtube.com/live2"
yt_key = "xxxxx"
stream_url = f"{yt_url}/{yt_key}"

ideo_dir = "videos"
video_index = ""
source = ""
video_scale = ""
index = 0
for file in os.listdir(video_dir):
    source += f'-i "{video_dir}/{file}" '
    video_scale += f"[{index}]scale=640x640,setdar=16/9[v{index}];"
    video_index += f"[v{index}][{index}:a]"
    index += 1

cmd = f'{source}-filter_complex "{video_scale} {video_index}concat=n={index}:v=1:a=1 [outv][outa]"'

command = f'ffmpeg {cmd} -map "[outv]" -map "[outa]" -f flv "{stream_url}"'
