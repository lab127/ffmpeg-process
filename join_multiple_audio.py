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


file_name = "test join audios"
audio_folder = "audio-video/songs"
file_dir = f"audio-video/output/{file_name}"
file_output = f"{file_dir}.mp3"

lst = os.listdir(audio_folder)
playlist = random_playlist(lst, 4)

audio_source = ""
audio_index = ""
index = 0

for file in playlist:
    audio_source += f'-i "{audio_folder}/{file}" '
    audio_index += f"[{index}:a]"
    index += 1

with open(f"{file_dir}.txt", "w", encoding="utf-8") as fp:
    for item in playlist:
        fp.write("%s\n" % item.replace(".mp3", ""))
    print("Ok")

# ok -
command = f'{audio_source}-filter_complex\
 "{audio_index}concat=n={index}:v=0:a=1"\
 "{file_output}"'

print(command)
os.system(f"ffmpeg {command}")
end = time()
print(f"{len(playlist)} songs in {(end-start)}s")
