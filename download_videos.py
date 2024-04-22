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
video_urls = ['https://www.youtube.com/shorts/LLk-_nHL_vA', 'https://www.youtube.com/shorts/LLk-_nHL_vA', 'https://www.youtube.com/shorts/aX6LsIn-6Rg', 'https://www.youtube.com/shorts/aX6LsIn-6Rg', 'https://www.youtube.com/shorts/62rQtmCNBPE', 'https://www.youtube.com/shorts/62rQtmCNBPE', 'https://www.youtube.com/shorts/M5d3XkV_5DY', 'https://www.youtube.com/shorts/M5d3XkV_5DY', 'https://www.youtube.com/shorts/A92yzH4Lpvs', 'https://www.youtube.com/shorts/A92yzH4Lpvs', 'https://www.youtube.com/shorts/JEOcN_ciUa0', 'https://www.youtube.com/shorts/JEOcN_ciUa0', 'https://www.youtube.com/shorts/bZqvPhkB09o', 'https://www.youtube.com/shorts/bZqvPhkB09o', 'https://www.youtube.com/shorts/0hf9oC__9f8', 'https://www.youtube.com/shorts/0hf9oC__9f8', 'https://www.youtube.com/shorts/CWrUwdbow9o', 'https://www.youtube.com/shorts/CWrUwdbow9o', 'https://www.youtube.com/shorts/3pZeE8ZA0YQ', 'https://www.youtube.com/shorts/3pZeE8ZA0YQ', 'https://www.youtube.com/shorts/bSwajjh3uTc', 'https://www.youtube.com/shorts/bSwajjh3uTc', 'https://www.youtube.com/shorts/pjWaAc35yhg', 'https://www.youtube.com/shorts/pjWaAc35yhg', 'https://www.youtube.com/shorts/DnCQ_XyekUI', 'https://www.youtube.com/shorts/DnCQ_XyekUI', 'https://www.youtube.com/shorts/n85LoJ_qn8I', 'https://www.youtube.com/shorts/n85LoJ_qn8I', 'https://www.youtube.com/shorts/RHe4-7q4jbQ', 'https://www.youtube.com/shorts/RHe4-7q4jbQ', 'https://www.youtube.com/shorts/k22TEVWUZXM', 'https://www.youtube.com/shorts/k22TEVWUZXM', 'https://www.youtube.com/shorts/15iAJDmwXHU', 'https://www.youtube.com/shorts/15iAJDmwXHU', 'https://www.youtube.com/shorts/0dIo1qZXrZE', 'https://www.youtube.com/shorts/0dIo1qZXrZE', 'https://www.youtube.com/shorts/vBrXxeZ6H8w', 'https://www.youtube.com/shorts/vBrXxeZ6H8w', 'https://www.youtube.com/shorts/rIh4qfh2MxA', 'https://www.youtube.com/shorts/rIh4qfh2MxA', 'https://www.youtube.com/shorts/4U5IwOFm7Vc', 'https://www.youtube.com/shorts/4U5IwOFm7Vc', 'https://www.youtube.com/shorts/ZdRFCrI0SbU', 'https://www.youtube.com/shorts/ZdRFCrI0SbU', 'https://www.youtube.com/shorts/AB2DaTOcCdA', 'https://www.youtube.com/shorts/AB2DaTOcCdA', 'https://www.youtube.com/shorts/vXszAEv-uAU', 'https://www.youtube.com/shorts/vXszAEv-uAU', 'https://www.youtube.com/shorts/5HjKmDhqSfg', 'https://www.youtube.com/shorts/5HjKmDhqSfg', 'https://www.youtube.com/shorts/AKpKBp_v9EA', 'https://www.youtube.com/shorts/AKpKBp_v9EA', 'https://www.youtube.com/shorts/WjCXP4d4qGU', 'https://www.youtube.com/shorts/WjCXP4d4qGU', 'https://www.youtube.com/shorts/kFcgO5zGy88', 'https://www.youtube.com/shorts/kFcgO5zGy88', 'https://www.youtube.com/shorts/7ilwMPd03yg', 'https://www.youtube.com/shorts/7ilwMPd03yg', 'https://www.youtube.com/shorts/rLaCUVSOi-k', 'https://www.youtube.com/shorts/rLaCUVSOi-k', 'https://www.youtube.com/shorts/sXN9t0dUJMo', 'https://www.youtube.com/shorts/sXN9t0dUJMo', 'https://www.youtube.com/shorts/n1TmXOZJ4H4', 'https://www.youtube.com/shorts/n1TmXOZJ4H4', 'https://www.youtube.com/shorts/btl1SToJ63c', 'https://www.youtube.com/shorts/btl1SToJ63c', 'https://www.youtube.com/shorts/bYp35Hqpg0g', 'https://www.youtube.com/shorts/bYp35Hqpg0g', 'https://www.youtube.com/shorts/DTsZa_xHGeQ', 'https://www.youtube.com/shorts/DTsZa_xHGeQ', 'https://www.youtube.com/shorts/gCEIiQ0o6gA', 'https://www.youtube.com/shorts/gCEIiQ0o6gA', 'https://www.youtube.com/shorts/RpvM3FSsIM4', 'https://www.youtube.com/shorts/RpvM3FSsIM4', 'https://www.youtube.com/shorts/f_uSprAtnHc', 'https://www.youtube.com/shorts/f_uSprAtnHc']


download_folder = 'VirallyRay'  # Customize your download folder
download_videos(video_urls, download_folder)