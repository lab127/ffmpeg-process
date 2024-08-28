ffmpeg -y \
-f concat -safe 0 -i input.txt \
-i image1.jpg \
-filter_complex \
"[0:a]showwaves=s=600x100:colors=white|red|blue:draw=full:mode=line,format=argb[wave];\
[0:v]scale=1280:720[fg];\
[fg][wave]overlay=x=(W-w)/2:y=H-h-20[with_overlay];\
[with_overlay]drawtext=text='%{metadata\:title}'\
:x=w-text_w-10:y=10\
:fontcolor=white:fontsize=48:bordercolor=black:borderw=2[txt];\
[txt]colorkey=0x80FF80:similarity=0.1[v1];\
[1:v]scale=1280:720[scaled_image];\
[scaled_image][v1]overlay" \
-map 0:v:0 -map 0:a:0 \
-c:v libx264 -preset superfast -c:a aac -ar 44100 -b:a 128k -pix_fmt yuv420p green-output.mp4