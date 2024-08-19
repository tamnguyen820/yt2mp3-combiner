import yt_dlp
from pydub import AudioSegment
import os
import re


def sanitize_filename(name):
    # Replace invalid characters with an underscore or remove them
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def download_youtube_video_to_mp3(url, output_path):
    with yt_dlp.YoutubeDL() as ydl:
        # Extract information first to get the sanitized title
        info_dict = ydl.extract_info(url, download=False)
        original_title = info_dict["title"]
        sanitized_title = sanitize_filename(original_title)

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_path, f"{sanitized_title}.%(ext)s"),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        # Now download using the sanitized title
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        audio_file = os.path.join(output_path, f"{sanitized_title}.mp3")
        return audio_file


def merge_mp3_files(mp3_files, output_path):
    combined = AudioSegment.from_mp3(mp3_files[0])
    for mp3_file in mp3_files[1:]:
        combined += AudioSegment.from_mp3(mp3_file)
    combined.export(output_path, format="mp3")


def main():
    input_file = "youtubelinks.txt"
    output_dir = "downloads"
    output_file = "combined.mp3"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mp3_files = []
    with open(input_file, "r") as file:
        for line in file:
            url = line.strip()
            if url:
                print(f"Downloading {url}")
                mp3_file = download_youtube_video_to_mp3(url, output_dir)
                mp3_files.append(mp3_file)

    if mp3_files:
        print("Merging MP3 files...")
        merge_mp3_files(mp3_files, os.path.join(output_dir, output_file))
        print(f"Combined MP3 saved as {os.path.join(output_dir, output_file)}")


if __name__ == "__main__":
    main()
