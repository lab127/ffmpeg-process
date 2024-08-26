import os

audiofile = "audio-video/audio/music.mp3"
ouputfile = "audio-video/output/out_waveform.mp4"
imagefile = "audio-video/images/ai-generated.jpg"

command4 = f' -y -i "{audiofile}" -loop 1 -i "{imagefile}" -filter_complex "[1:v]scale=1280:-2[bg];[0:a]compand,showwaves=size=1280x200:colors=#25d3d0|#7925d3:draw=full:mode=line,format=argb[v];[bg][v]overlay=0:H-200,drawtext=fontcolor=white:x=10:y=10:text=\'Song Title by Artist\':fontsize=24:bordercolor=black:borderw=2[outv]" -map "[outv]" -pix_fmt yuv420p -map 0:a -c:v libx264 -c:a copy -shortest "{ouputfile}--command4-img4267x6400.mp4"'

os.system(f"ffmpeg {command4}")
