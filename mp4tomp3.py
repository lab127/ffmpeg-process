import os


def convert_mp3(input_dir, output_dir):
    for f in os.listdir(input_dir):
        filename, _ = os.path.splitext(f)
        input_file = f"{input_dir}/{f}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = f"{output_dir}/{filename}.mp3"
        cmd = f'ffmpeg -i "{input_file}" -vn -c:a libmp3lame -y "{output_file}"'
        os.system(cmd)


convert_mp3("video", "audio")
