from pytube import YouTube
import whisper
import os
import re

def sanitize_filename(filename):
    """Remove or replace characters in a string to make it a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", filename)  # Removes problematic characters

def transcribe_video(video_url, output_folder="transcribed_files"):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    yt = YouTube(video_url)
    title = sanitize_filename(yt.title)
    audio_stream = yt.streams.get_audio_only()
    audio_stream.download(filename="temp_audio.mp4")

    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.mp4")
    
    # Adjust the file path to include the output folder
    output_path = os.path.join(output_folder, f"{title}.txt")
    with open(output_path, "w") as f:
        f.write(result["text"])
    
    os.remove("temp_audio.mp4")
    print(f"Transcription for '{title}' saved in '{output_folder}' folder.")

video_urls = ['https://www.youtube.com/shorts/Kb88OYITHoU', 'https://www.youtube.com/shorts/Kb88OYITHoU', 'https://www.youtube.com/shorts/9bZ388oTH4o']

for url in video_urls:
    transcribe_video(url)

