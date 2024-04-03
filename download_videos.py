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
video_urls = video_urls = ['https://www.youtube.com/shorts/IdnEDDWg3TM', 'https://www.youtube.com/shorts/IdnEDDWg3TM', 'https://www.youtube.com/shorts/oAbkhSNpQpI', 'https://www.youtube.com/shorts/oAbkhSNpQpI', 'https://www.youtube.com/shorts/fOCDASeGpY8', 'https://www.youtube.com/shorts/fOCDASeGpY8', 'https://www.youtube.com/shorts/QNwE0POTcKk', 'https://www.youtube.com/shorts/QNwE0POTcKk', 'https://www.youtube.com/shorts/hGLKzwQnF3Y', 'https://www.youtube.com/shorts/hGLKzwQnF3Y', 'https://www.youtube.com/shorts/euIEuxPZeyQ', 'https://www.youtube.com/shorts/euIEuxPZeyQ', 'https://www.youtube.com/shorts/ts6Tm69Iebo', 'https://www.youtube.com/shorts/ts6Tm69Iebo', 'https://www.youtube.com/shorts/D_iGOt9f1sk', 'https://www.youtube.com/shorts/D_iGOt9f1sk', 'https://www.youtube.com/shorts/PHTD6DcpbKM', 'https://www.youtube.com/shorts/PHTD6DcpbKM', 'https://www.youtube.com/shorts/6dCGus-V634', 'https://www.youtube.com/shorts/6dCGus-V634', 'https://www.youtube.com/shorts/UMPHURq9G5I', 'https://www.youtube.com/shorts/UMPHURq9G5I', 'https://www.youtube.com/shorts/qT4KECVywcA', 'https://www.youtube.com/shorts/qT4KECVywcA', 'https://www.youtube.com/shorts/FNUWYrqEd8U', 'https://www.youtube.com/shorts/FNUWYrqEd8U', 'https://www.youtube.com/shorts/DR1LWShyJFM', 'https://www.youtube.com/shorts/DR1LWShyJFM', 'https://www.youtube.com/shorts/vYyNjyD5Sfo', 'https://www.youtube.com/shorts/vYyNjyD5Sfo', 'https://www.youtube.com/shorts/WptgVMavDgc', 'https://www.youtube.com/shorts/WptgVMavDgc', 'https://www.youtube.com/shorts/TuvdqtNMNIo', 'https://www.youtube.com/shorts/TuvdqtNMNIo', 'https://www.youtube.com/shorts/c0t16RN4M1g', 'https://www.youtube.com/shorts/c0t16RN4M1g', 'https://www.youtube.com/shorts/ceLZzeTHKxk', 'https://www.youtube.com/shorts/ceLZzeTHKxk', 'https://www.youtube.com/shorts/6rl-RiToEjA', 'https://www.youtube.com/shorts/6rl-RiToEjA', 'https://www.youtube.com/shorts/EnxQ9tpa0HY', 'https://www.youtube.com/shorts/EnxQ9tpa0HY', 'https://www.youtube.com/shorts/M70bxjfBB2c', 'https://www.youtube.com/shorts/M70bxjfBB2c', 'https://www.youtube.com/shorts/bSRwwTysEsY', 'https://www.youtube.com/shorts/bSRwwTysEsY', 'https://www.youtube.com/shorts/zP-C88GJKyU', 'https://www.youtube.com/shorts/zP-C88GJKyU', 'https://www.youtube.com/shorts/XTJ2U02gX-s', 'https://www.youtube.com/shorts/XTJ2U02gX-s', 'https://www.youtube.com/shorts/BH_smA4qUa4', 'https://www.youtube.com/shorts/BH_smA4qUa4', 'https://www.youtube.com/shorts/mEcLBjKAitE', 'https://www.youtube.com/shorts/mEcLBjKAitE', 'https://www.youtube.com/shorts/-eQ5gM__xWs', 'https://www.youtube.com/shorts/-eQ5gM__xWs', 'https://www.youtube.com/shorts/ESKzUEOw-nQ', 'https://www.youtube.com/shorts/ESKzUEOw-nQ', 'https://www.youtube.com/shorts/LiRC9KbvASo', 'https://www.youtube.com/shorts/LiRC9KbvASo', 'https://www.youtube.com/shorts/KmenSidDlys', 'https://www.youtube.com/shorts/KmenSidDlys', 'https://www.youtube.com/shorts/nEMFpd6Q_n0', 'https://www.youtube.com/shorts/nEMFpd6Q_n0', 'https://www.youtube.com/shorts/m9ifb2MLzPA', 'https://www.youtube.com/shorts/m9ifb2MLzPA', 'https://www.youtube.com/shorts/WPZLaY6OUe8', 'https://www.youtube.com/shorts/WPZLaY6OUe8', 'https://www.youtube.com/shorts/fAdN-uCktTo', 'https://www.youtube.com/shorts/fAdN-uCktTo', 'https://www.youtube.com/shorts/xtCIEdepLbo', 'https://www.youtube.com/shorts/xtCIEdepLbo', 'https://www.youtube.com/shorts/e2kqJjwxZZE', 'https://www.youtube.com/shorts/e2kqJjwxZZE', 'https://www.youtube.com/shorts/cfVky6DtAgo', 'https://www.youtube.com/shorts/cfVky6DtAgo', 'https://www.youtube.com/shorts/lFROh3_NiS8', 'https://www.youtube.com/shorts/lFROh3_NiS8', 'https://www.youtube.com/shorts/iX4Knbhwi7I', 'https://www.youtube.com/shorts/iX4Knbhwi7I', 'https://www.youtube.com/shorts/bHYv46SusCY', 'https://www.youtube.com/shorts/bHYv46SusCY', 'https://www.youtube.com/shorts/yt-O6CxqZiY', 'https://www.youtube.com/shorts/yt-O6CxqZiY', 'https://www.youtube.com/shorts/VVaqgCO9T44', 'https://www.youtube.com/shorts/VVaqgCO9T44', 'https://www.youtube.com/shorts/h-UmspjMvj4', 'https://www.youtube.com/shorts/h-UmspjMvj4', 'https://www.youtube.com/shorts/GEY_fw3yJP0', 'https://www.youtube.com/shorts/GEY_fw3yJP0', 'https://www.youtube.com/shorts/hpAeRqia68o', 'https://www.youtube.com/shorts/hpAeRqia68o']



download_folder = 'thevon'  # Customize your download folder
download_videos(video_urls, download_folder)