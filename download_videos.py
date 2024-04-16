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
video_urls =['https://www.youtube.com/shorts/UaphU0Rdp08', 'https://www.youtube.com/shorts/UaphU0Rdp08', 'https://www.youtube.com/shorts/HtAdpEV4dcY', 'https://www.youtube.com/shorts/HtAdpEV4dcY', 'https://www.youtube.com/shorts/gZQw-RI6sNY', 'https://www.youtube.com/shorts/gZQw-RI6sNY', 'https://www.youtube.com/shorts/Qhcfkwa2mbE', 'https://www.youtube.com/shorts/Qhcfkwa2mbE', 'https://www.youtube.com/shorts/jRNwqK8748o', 'https://www.youtube.com/shorts/jRNwqK8748o', 'https://www.youtube.com/shorts/DfdYBpGlNqo', 'https://www.youtube.com/shorts/DfdYBpGlNqo', 'https://www.youtube.com/shorts/FTIf996a-q4', 'https://www.youtube.com/shorts/FTIf996a-q4', 'https://www.youtube.com/shorts/Q1DYjH7Oqj0', 'https://www.youtube.com/shorts/Q1DYjH7Oqj0', 'https://www.youtube.com/shorts/vVbnUQb6abE', 'https://www.youtube.com/shorts/vVbnUQb6abE', 'https://www.youtube.com/shorts/G3WCvjKE33c', 'https://www.youtube.com/shorts/G3WCvjKE33c', 'https://www.youtube.com/shorts/-1JuGRWZ918', 'https://www.youtube.com/shorts/-1JuGRWZ918', 'https://www.youtube.com/shorts/JqFp1ZxTxgQ', 'https://www.youtube.com/shorts/JqFp1ZxTxgQ', 'https://www.youtube.com/shorts/ROtriB4C-OU', 'https://www.youtube.com/shorts/ROtriB4C-OU', 'https://www.youtube.com/shorts/sPbMEs7PGfE', 'https://www.youtube.com/shorts/sPbMEs7PGfE', 'https://www.youtube.com/shorts/zcofhDYEyPc', 'https://www.youtube.com/shorts/zcofhDYEyPc', 'https://www.youtube.com/shorts/y98jHvSnlYM', 'https://www.youtube.com/shorts/y98jHvSnlYM', 'https://www.youtube.com/shorts/J4QySG0Ovck', 'https://www.youtube.com/shorts/J4QySG0Ovck', 'https://www.youtube.com/shorts/ixy6JUH_1Bg', 'https://www.youtube.com/shorts/ixy6JUH_1Bg', 'https://www.youtube.com/shorts/s5OcW6kf9TE', 'https://www.youtube.com/shorts/s5OcW6kf9TE', 'https://www.youtube.com/shorts/MdHi9M9Vcic', 'https://www.youtube.com/shorts/MdHi9M9Vcic', 'https://www.youtube.com/shorts/KpXqTdp8vXg', 'https://www.youtube.com/shorts/KpXqTdp8vXg', 'https://www.youtube.com/shorts/nBzQY5aj1yU', 'https://www.youtube.com/shorts/nBzQY5aj1yU', 'https://www.youtube.com/shorts/GCNs8UYLCt0', 'https://www.youtube.com/shorts/GCNs8UYLCt0', 'https://www.youtube.com/shorts/0otlJGXyr9E', 'https://www.youtube.com/shorts/0otlJGXyr9E', 'https://www.youtube.com/shorts/K5ZeUDJcyTg', 'https://www.youtube.com/shorts/K5ZeUDJcyTg', 'https://www.youtube.com/shorts/ygg2XvI2LuE', 'https://www.youtube.com/shorts/ygg2XvI2LuE', 'https://www.youtube.com/shorts/ksy2lksngJs', 'https://www.youtube.com/shorts/ksy2lksngJs', 'https://www.youtube.com/shorts/ivfzvmNEEkE', 'https://www.youtube.com/shorts/ivfzvmNEEkE', 'https://www.youtube.com/shorts/5PUZPR3tMKA', 'https://www.youtube.com/shorts/5PUZPR3tMKA', 'https://www.youtube.com/shorts/4Xv1BAR3dV4', 'https://www.youtube.com/shorts/4Xv1BAR3dV4', 'https://www.youtube.com/shorts/t4NlY3Pn3go', 'https://www.youtube.com/shorts/t4NlY3Pn3go', 'https://www.youtube.com/shorts/xWPx9Df-vxU', 'https://www.youtube.com/shorts/xWPx9Df-vxU', 'https://www.youtube.com/shorts/XNA25dxomm0', 'https://www.youtube.com/shorts/XNA25dxomm0', 'https://www.youtube.com/shorts/Xko2VwP7ii0', 'https://www.youtube.com/shorts/Xko2VwP7ii0', 'https://www.youtube.com/shorts/io-meYmUnwE', 'https://www.youtube.com/shorts/io-meYmUnwE', 'https://www.youtube.com/shorts/XtnsxdPLDFk', 'https://www.youtube.com/shorts/XtnsxdPLDFk', 'https://www.youtube.com/shorts/adyP1v1-cfo', 'https://www.youtube.com/shorts/adyP1v1-cfo', 'https://www.youtube.com/shorts/wrjtYKbYMyQ', 'https://www.youtube.com/shorts/wrjtYKbYMyQ', 'https://www.youtube.com/shorts/UJBODxabsYY', 'https://www.youtube.com/shorts/UJBODxabsYY']

download_folder = 'plasticinerelax'  # Customize your download folder
download_videos(video_urls, download_folder)