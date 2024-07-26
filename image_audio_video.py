import os

image = "image.png"
audio = "audio.mp3"
output = "out.mp4"
cmd = f"ffmpeg -loop 1 -i {image} -i {audio} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest {output}"

os.system(cmd)