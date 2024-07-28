#!/bin/bash
# https://stackoverflow.com/questions/77185449/how-to-stream-24-7-on-youtube-audio-video-with-ffmpeg

VBR="4500k"
FPS="30"
QUAL="superfast"

YOUTUBE_URL="rtmp://a.rtmp.youtube.com/live2"
KEY="XXXX-XXXX-XXXX-XXXX"

VIDEO_SOURCE="fireplace.mkv"
AUDIO_FOLDER="/home/administrateur/Documents/Youtube/Playlist"

while true; do
    # ffmpeg seharusnya diluar loop, kalau tidak tiap lagu akan stop
    ffmpeg -re -stream_loop -1 -i "$VIDEO_SOURCE" \
    -thread_queue_size 512 -i "$(find "$AUDIO_FOLDER" -type f -name "*.mp3" | shuf -n 1)" \
    -map 0:v:0 -map 1:a:0 \
    -map_metadata:g 1:g \
    -vcodec libx264 -pix_fmt yuv420p -preset $QUAL -r $FPS -g $(($FPS * 2)) -b:v $VBR \
    -acodec libmp3lame -ar 44100 -threads 6 -qscale:v 3 -b:a 320000 -bufsize 512k \
    -f flv "$YOUTUBE_URL/$KEY"
done

ffmpeg -re -loop 1 -i "/content/drive/My Drive//images/wallhaven-d6y12l.jpg" -i "/content/drive/My Drive//audio/Sleep - KaizanBlu.mp3" -i "/content/drive/My Drive//audio/Sleep Away by Evol.mp3" -i "/content/drive/My Drive//audio/Soul Aches by Yakuzee Beatz.mp3" -i "/content/drive/My Drive//audio/Stay - KaizanBlu (No Copyright) Chill Relaxing LoFi HipHop Music [No Copyright Music].mp3" -i "/content/drive/My Drive//audio/Swan Mother by Homie Cat.mp3" -filter_complex "[0:v]scale=1280:720[v];[1:0][2:0][3:0][4:0][5:0]concat=n=5:v=0:a=1[outa]" -map "[v]" -map "[outa]" -vcodec libx264 -preset superfast -b:v 2500k -pix_fmt yuv420p -r 30 -g 60 -acodec libmp3lame -ar 44100 -threads 6 -qscale:v 3 -b:a 128k -bufsize 512k -f flv "rtmp://a.rtmp.youtube.com/live2/8t6r-m4ek-mzp4-kscw-fx68"
