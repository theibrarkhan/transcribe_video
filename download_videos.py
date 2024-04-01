from pytube import YouTube
import os
import time



def download_videos(video_urls, download_folder='youtubevideos'):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    for url in video_urls:
        try:
            yt = YouTube(url)
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video_stream.download(download_folder)
            print(f"Downloaded: {yt.title}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    print("All videos have been downloaded.")

# Example usage
shorts_url = 'https://www.youtube.com/@AdinRoss/shorts'
video_urls = video_urls = ['https://www.youtube.com/shorts/Kb88OYITHoU', 'https://www.youtube.com/shorts/Kb88OYITHoU', 'https://www.youtube.com/shorts/9bZ388oTH4o', 'https://www.youtube.com/shorts/9bZ388oTH4o', 'https://www.youtube.com/shorts/k1qnCKWaN74', 'https://www.youtube.com/shorts/k1qnCKWaN74', 'https://www.youtube.com/shorts/XqY_GzKcWbw']
download_folder = 'AdinRoss'  # Customize your download folder
download_videos(video_urls, download_folder)