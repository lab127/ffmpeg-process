import os

video_dir = "videos"
video_index = ""
source = ""
video_scale = ""
index = 0
for file in os.listdir(video_dir):
    source += f'-i "{video_dir}/{file}" '
    video_scale += f'[{index}]scale=640x640,setdar=16/9[v{index}];'
    video_index += f'[v{index}][{index}:a]'
    index += 1

cmd = f'ffmpeg {source}-filter_complex \
"{video_scale} \
{video_index}concat=n={index}:v=1:a=1 [outv][outa]" \
-map "[outv]" -map "[outa]" output2.mp4'
print(cmd)
# os.system(cmd)


# ffmpeg -i new1.mp4 -i new2.mp4 -i new3.mp4 -i new4.mp4 -filter_complex \
#         "[0]setdar=16/9[a];[1]setdar=16/9[b];[2]setdar=16/9[c];[3]setdar=16/9[d]; \
#          [a][b][c][d]concat=n=4:v=1:a=1" output.mp4