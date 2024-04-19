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
# shorts_url = 'https://www.youtube.com/@AdinRoss/shorts'
video_urls = ['https://www.youtube.com/shorts/HlcUl5-AJxo', 'https://www.youtube.com/shorts/HlcUl5-AJxo', 'https://www.youtube.com/shorts/gjn9tPIHM9A', 'https://www.youtube.com/shorts/gjn9tPIHM9A', 'https://www.youtube.com/shorts/ZMnWPslac2w', 'https://www.youtube.com/shorts/ZMnWPslac2w', 'https://www.youtube.com/shorts/7vMrbambnHA', 'https://www.youtube.com/shorts/7vMrbambnHA', 'https://www.youtube.com/shorts/FHZTRe7480g', 'https://www.youtube.com/shorts/FHZTRe7480g', 'https://www.youtube.com/shorts/L2Om20AryVQ', 'https://www.youtube.com/shorts/L2Om20AryVQ', 'https://www.youtube.com/shorts/--qI8YLyaQ4', 'https://www.youtube.com/shorts/--qI8YLyaQ4', 'https://www.youtube.com/shorts/TPwuW_kEKsE', 'https://www.youtube.com/shorts/TPwuW_kEKsE', 'https://www.youtube.com/shorts/-x5xYgQNWJk', 'https://www.youtube.com/shorts/-x5xYgQNWJk', 'https://www.youtube.com/shorts/OVIosG_qYgQ', 'https://www.youtube.com/shorts/OVIosG_qYgQ', 'https://www.youtube.com/shorts/Gvd_F8kE_a4', 'https://www.youtube.com/shorts/Gvd_F8kE_a4', 'https://www.youtube.com/shorts/_B4gKMbZ_x0', 'https://www.youtube.com/shorts/_B4gKMbZ_x0', 'https://www.youtube.com/shorts/nM8e5jD5fSM', 'https://www.youtube.com/shorts/nM8e5jD5fSM', 'https://www.youtube.com/shorts/GwbP9JBOFK4', 'https://www.youtube.com/shorts/GwbP9JBOFK4', 'https://www.youtube.com/shorts/axHYYg2idBI', 'https://www.youtube.com/shorts/axHYYg2idBI', 'https://www.youtube.com/shorts/uidCBdLWt7M', 'https://www.youtube.com/shorts/uidCBdLWt7M', 'https://www.youtube.com/shorts/1MA2rNUVvcs', 'https://www.youtube.com/shorts/1MA2rNUVvcs', 'https://www.youtube.com/shorts/KanddyjzH1o', 'https://www.youtube.com/shorts/KanddyjzH1o', 'https://www.youtube.com/shorts/py3Vym-Gw3o', 'https://www.youtube.com/shorts/py3Vym-Gw3o', 'https://www.youtube.com/shorts/TD3KtZAtzRE', 'https://www.youtube.com/shorts/TD3KtZAtzRE', 'https://www.youtube.com/shorts/8hJaCtyXazs', 'https://www.youtube.com/shorts/8hJaCtyXazs', 'https://www.youtube.com/shorts/QVbSpHJGyyg', 'https://www.youtube.com/shorts/QVbSpHJGyyg', 'https://www.youtube.com/shorts/N5K2NrRam9E', 'https://www.youtube.com/shorts/N5K2NrRam9E', 'https://www.youtube.com/shorts/gcR6s9EJ_3g', 'https://www.youtube.com/shorts/gcR6s9EJ_3g', 'https://www.youtube.com/shorts/iMhGrOJM8EA', 'https://www.youtube.com/shorts/iMhGrOJM8EA', 'https://www.youtube.com/shorts/X4R-gXuilLg', 'https://www.youtube.com/shorts/X4R-gXuilLg', 'https://www.youtube.com/shorts/THS5ePmXaFo', 'https://www.youtube.com/shorts/THS5ePmXaFo', 'https://www.youtube.com/shorts/NKVvQV4NT2s', 'https://www.youtube.com/shorts/NKVvQV4NT2s', 'https://www.youtube.com/shorts/x6t4mhbUZiE', 'https://www.youtube.com/shorts/x6t4mhbUZiE', 'https://www.youtube.com/shorts/7VYBcxdAzMI', 'https://www.youtube.com/shorts/7VYBcxdAzMI', 'https://www.youtube.com/shorts/uPqPgrGqPWc', 'https://www.youtube.com/shorts/uPqPgrGqPWc', 'https://www.youtube.com/shorts/FMk9VBtDlHo', 'https://www.youtube.com/shorts/FMk9VBtDlHo', 'https://www.youtube.com/shorts/pukuePjf94U', 'https://www.youtube.com/shorts/pukuePjf94U', 'https://www.youtube.com/shorts/C4XfeXAAioQ', 'https://www.youtube.com/shorts/C4XfeXAAioQ', 'https://www.youtube.com/shorts/juN5lQ_ya4I', 'https://www.youtube.com/shorts/juN5lQ_ya4I', 'https://www.youtube.com/shorts/iot4h0hxxQI', 'https://www.youtube.com/shorts/iot4h0hxxQI', 'https://www.youtube.com/shorts/CylT9yO8hSw', 'https://www.youtube.com/shorts/CylT9yO8hSw', 'https://www.youtube.com/shorts/8JXlRkPbOEw', 'https://www.youtube.com/shorts/8JXlRkPbOEw', 'https://www.youtube.com/shorts/gT0XrCfM39g', 'https://www.youtube.com/shorts/gT0XrCfM39g', 'https://www.youtube.com/shorts/EC3O-dKQdxE', 'https://www.youtube.com/shorts/EC3O-dKQdxE', 'https://www.youtube.com/shorts/qdekymddJ_c', 'https://www.youtube.com/shorts/qdekymddJ_c', 'https://www.youtube.com/shorts/PMRvjiIW2CM', 'https://www.youtube.com/shorts/PMRvjiIW2CM', 'https://www.youtube.com/shorts/ION9q_c7mTI', 'https://www.youtube.com/shorts/ION9q_c7mTI', 'https://www.youtube.com/shorts/LIzcE9hcN48', 'https://www.youtube.com/shorts/LIzcE9hcN48', 'https://www.youtube.com/shorts/6xYv7Sa8jrI', 'https://www.youtube.com/shorts/6xYv7Sa8jrI', 'https://www.youtube.com/shorts/pViD19gGXfE', 'https://www.youtube.com/shorts/pViD19gGXfE', 'https://www.youtube.com/shorts/KCvT54EPfHU', 'https://www.youtube.com/shorts/KCvT54EPfHU', 'https://www.youtube.com/shorts/23MKnh6rW18', 'https://www.youtube.com/shorts/23MKnh6rW18', 'https://www.youtube.com/shorts/tPcm2PUHyZk', 'https://www.youtube.com/shorts/tPcm2PUHyZk', 'https://www.youtube.com/shorts/T-GiAQqtSgM', 'https://www.youtube.com/shorts/T-GiAQqtSgM']

download_folder = 'Emiru'  # Customize your download folder
download_videos(video_urls, download_folder)