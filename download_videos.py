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
video_urls = ['https://www.youtube.com/shorts/ej1IgaG2cL8', 'https://www.youtube.com/shorts/ej1IgaG2cL8', 'https://www.youtube.com/shorts/mEGJuhI1Loc', 'https://www.youtube.com/shorts/mEGJuhI1Loc', 'https://www.youtube.com/shorts/Hl-WfOs1ne4', 'https://www.youtube.com/shorts/Hl-WfOs1ne4', 'https://www.youtube.com/shorts/90db8ASxDrk', 'https://www.youtube.com/shorts/90db8ASxDrk', 'https://www.youtube.com/shorts/Z6GE38jS3Ds', 'https://www.youtube.com/shorts/Z6GE38jS3Ds', 'https://www.youtube.com/shorts/g-e16H2leY4', 'https://www.youtube.com/shorts/g-e16H2leY4', 'https://www.youtube.com/shorts/XHTkZ4cX5gs', 'https://www.youtube.com/shorts/XHTkZ4cX5gs', 'https://www.youtube.com/shorts/bre9RF2Q0Yc', 'https://www.youtube.com/shorts/bre9RF2Q0Yc', 'https://www.youtube.com/shorts/p1yZrRflESY', 'https://www.youtube.com/shorts/p1yZrRflESY', 'https://www.youtube.com/shorts/9uQ-hT6lLiI', 'https://www.youtube.com/shorts/9uQ-hT6lLiI', 'https://www.youtube.com/shorts/rDSjibGHJew', 'https://www.youtube.com/shorts/rDSjibGHJew', 'https://www.youtube.com/shorts/TBCW65jnbxI', 'https://www.youtube.com/shorts/TBCW65jnbxI', 'https://www.youtube.com/shorts/uhjXz3_YPQw', 'https://www.youtube.com/shorts/uhjXz3_YPQw', 'https://www.youtube.com/shorts/ds_Tl-qXYow', 'https://www.youtube.com/shorts/ds_Tl-qXYow', 'https://www.youtube.com/shorts/C8Yx-WCoSNM', 'https://www.youtube.com/shorts/C8Yx-WCoSNM', 'https://www.youtube.com/shorts/jmNwYrcQEa0', 'https://www.youtube.com/shorts/jmNwYrcQEa0', 'https://www.youtube.com/shorts/25vPSmptIns', 'https://www.youtube.com/shorts/25vPSmptIns', 'https://www.youtube.com/shorts/IBYnz1OEVKo', 'https://www.youtube.com/shorts/IBYnz1OEVKo', 'https://www.youtube.com/shorts/wKtTFuryV_I', 'https://www.youtube.com/shorts/wKtTFuryV_I', 'https://www.youtube.com/shorts/iWK1hU7X4rE', 'https://www.youtube.com/shorts/iWK1hU7X4rE']


download_folder = 'DavidAlvareeezy'  # Customize your download folder
download_videos(video_urls, download_folder)