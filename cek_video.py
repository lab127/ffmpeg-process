import os

video_dir = "videos"
video_index = ""
source = ""
video_scale = ""
index = 0
for file in os.listdir(video_dir):
    source += f'-i "{video_dir}/{file}" '
    video_scale += f'[{index}:v] scale=1280:720:force_original_aspect_ratio=decrease:eval=frame,pad=1280:720:-1:-1:color=black[v{index}]; '
    # video_index += f'[{index}:v:0] [{index}:a:0] '
    video_index += f'[v{index}][{index}:a]'
    index += 1

command = f'{source}-filter_complex "{video_scale}{video_index} concat=n={index}:v=1:a=1 [v] [a]" -map [v] -map [a] -s hd720 -vcodec libx264'
# command = f'{source}-filter_complex "{video_index}concat=n={index}:v=1:a=1 [outv] [outa]"'
print(command)

# command = f'{source}\
# -filter_complex "{video_index}concat=n={index}:v=1:a=1[outv][outa]" \
# -map "[outv]" -map "[outa]" \
# -vcodec libx264 -pix_fmt yuv420p -preset medium -r 30 -g 60 -b:v 2500k \
# -acodec libmp3lame -ar 44100 -threads 6 -qscale 3 -b:a 712000 -bufsize 512k'

# [0:v] scale=1280:720:force_original_aspect_ratio=decrease:eval=frame,pad=1280:720:-1:-1:color=black[v0];[1:v] scale=1280:720:force_original_aspect_ratio=decrease:eval=frame,pad=1280:720:-1:-1:color=black[v1];

# ffmpeg -i 1.mp4 -i 2.mp4 -n -filter_complex "[0:v]scale=1280:720:force_original_aspect_ratio=decrease:eval=frame,pad=1280:720:-1:-1:color=black[v0]; [1:v]scale=1280:720:force_original_aspect_ratio=decrease:eval=frame,pad=1280:720:-1:-1:color=black[v1]; [v0][0:a][v1][1:a] concat=n=2:v=1:a=1 [v] [a]" -map [v] -map [a] -s hd720 -vcodec libx264 result1.mp4

# -i videos/input1.mp4 -i videos/input2.mp4 -filter_complex ' [0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]'
# -i 'videos/input1.mp4' -i 'videos/input2.mp4' -filter_complex '[0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]'