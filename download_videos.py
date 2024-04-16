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
video_urls =['https://www.youtube.com/shorts/7D6taz-oZEc', 'https://www.youtube.com/shorts/7D6taz-oZEc', 'https://www.youtube.com/shorts/2H6XobslMfo', 'https://www.youtube.com/shorts/2H6XobslMfo', 'https://www.youtube.com/shorts/x_QCL6DLhIQ', 'https://www.youtube.com/shorts/x_QCL6DLhIQ', 'https://www.youtube.com/shorts/y6e5IawOEpA', 'https://www.youtube.com/shorts/y6e5IawOEpA', 'https://www.youtube.com/shorts/t70KvEpvtWE', 'https://www.youtube.com/shorts/t70KvEpvtWE', 'https://www.youtube.com/shorts/JxQdxZJLPMg', 'https://www.youtube.com/shorts/JxQdxZJLPMg', 'https://www.youtube.com/shorts/F3NOVyYuJkk', 'https://www.youtube.com/shorts/F3NOVyYuJkk', 'https://www.youtube.com/shorts/U_nFZOlNk7M', 'https://www.youtube.com/shorts/U_nFZOlNk7M', 'https://www.youtube.com/shorts/BhNqCAw3O30', 'https://www.youtube.com/shorts/BhNqCAw3O30', 'https://www.youtube.com/shorts/d0JtFHDnZzg', 'https://www.youtube.com/shorts/d0JtFHDnZzg', 'https://www.youtube.com/shorts/iEugSZSnL9U', 'https://www.youtube.com/shorts/iEugSZSnL9U', 'https://www.youtube.com/shorts/pBHqf_pcshA', 'https://www.youtube.com/shorts/pBHqf_pcshA', 'https://www.youtube.com/shorts/D9uR6KUfzWU', 'https://www.youtube.com/shorts/D9uR6KUfzWU', 'https://www.youtube.com/shorts/96V5Gsiyo2Y', 'https://www.youtube.com/shorts/96V5Gsiyo2Y', 'https://www.youtube.com/shorts/ujO3FdUM7U4', 'https://www.youtube.com/shorts/ujO3FdUM7U4', 'https://www.youtube.com/shorts/PWBeL2UD36c', 'https://www.youtube.com/shorts/PWBeL2UD36c', 'https://www.youtube.com/shorts/aLsOBoY4jxc', 'https://www.youtube.com/shorts/aLsOBoY4jxc', 'https://www.youtube.com/shorts/YOo0XhN7klQ', 'https://www.youtube.com/shorts/YOo0XhN7klQ', 'https://www.youtube.com/shorts/PMQtTmbg4CY', 'https://www.youtube.com/shorts/PMQtTmbg4CY', 'https://www.youtube.com/shorts/jLUFc5fCWiI', 'https://www.youtube.com/shorts/jLUFc5fCWiI', 'https://www.youtube.com/shorts/FDOMDLWNyrw', 'https://www.youtube.com/shorts/FDOMDLWNyrw', 'https://www.youtube.com/shorts/gC7WQTxKop0', 'https://www.youtube.com/shorts/gC7WQTxKop0', 'https://www.youtube.com/shorts/s1t5xjebduY', 'https://www.youtube.com/shorts/s1t5xjebduY', 'https://www.youtube.com/shorts/YIRohNMAmOg', 'https://www.youtube.com/shorts/YIRohNMAmOg', 'https://www.youtube.com/shorts/wAKf2bBdDdI', 'https://www.youtube.com/shorts/wAKf2bBdDdI', 'https://www.youtube.com/shorts/N4EBadZykv4', 'https://www.youtube.com/shorts/N4EBadZykv4', 'https://www.youtube.com/shorts/KYJleb9cd08', 'https://www.youtube.com/shorts/KYJleb9cd08', 'https://www.youtube.com/shorts/yYJwjja6ixE', 'https://www.youtube.com/shorts/yYJwjja6ixE', 'https://www.youtube.com/shorts/QHimfuWKBTM', 'https://www.youtube.com/shorts/QHimfuWKBTM', 'https://www.youtube.com/shorts/e7hgK9wH4IU', 'https://www.youtube.com/shorts/e7hgK9wH4IU', 'https://www.youtube.com/shorts/YJyHtrvJM0M', 'https://www.youtube.com/shorts/YJyHtrvJM0M', 'https://www.youtube.com/shorts/WCw64JdMXl4', 'https://www.youtube.com/shorts/WCw64JdMXl4', 'https://www.youtube.com/shorts/wg5QwFzFbBw', 'https://www.youtube.com/shorts/wg5QwFzFbBw', 'https://www.youtube.com/shorts/B1W_INqnh74', 'https://www.youtube.com/shorts/B1W_INqnh74', 'https://www.youtube.com/shorts/Ww5Ngk89TFA', 'https://www.youtube.com/shorts/Ww5Ngk89TFA', 'https://www.youtube.com/shorts/qNpCuAOMLgA', 'https://www.youtube.com/shorts/qNpCuAOMLgA', 'https://www.youtube.com/shorts/NpeVxnPxBas', 'https://www.youtube.com/shorts/NpeVxnPxBas', 'https://www.youtube.com/shorts/bhA9y5tSDrQ', 'https://www.youtube.com/shorts/bhA9y5tSDrQ', 'https://www.youtube.com/shorts/6EFsJRkIK9o', 'https://www.youtube.com/shorts/6EFsJRkIK9o', 'https://www.youtube.com/shorts/f9r11mblSmk', 'https://www.youtube.com/shorts/f9r11mblSmk', 'https://www.youtube.com/shorts/_HYywxUZTkE', 'https://www.youtube.com/shorts/_HYywxUZTkE', 'https://www.youtube.com/shorts/0lFFxTK4cwA', 'https://www.youtube.com/shorts/0lFFxTK4cwA', 'https://www.youtube.com/shorts/i0TTVmS5hmg', 'https://www.youtube.com/shorts/i0TTVmS5hmg', 'https://www.youtube.com/shorts/SC1TzXdk2HA', 'https://www.youtube.com/shorts/SC1TzXdk2HA', 'https://www.youtube.com/shorts/pEEeDkHsNlI', 'https://www.youtube.com/shorts/pEEeDkHsNlI', 'https://www.youtube.com/shorts/zieTsxLIIzE', 'https://www.youtube.com/shorts/zieTsxLIIzE', 'https://www.youtube.com/shorts/42i_r606ZxM', 'https://www.youtube.com/shorts/42i_r606ZxM', 'https://www.youtube.com/shorts/rQ_uo9J4_n8', 'https://www.youtube.com/shorts/rQ_uo9J4_n8', 'https://www.youtube.com/shorts/os_kgnmuvl4', 'https://www.youtube.com/shorts/os_kgnmuvl4', 'https://www.youtube.com/shorts/VxijCpzwVTQ', 'https://www.youtube.com/shorts/VxijCpzwVTQ','https://www.youtube.com/shorts/tiKNbc2YD8o', 'https://www.youtube.com/shorts/tiKNbc2YD8o', 'https://www.youtube.com/shorts/78i4Hcs9Zec', 'https://www.youtube.com/shorts/78i4Hcs9Zec', 'https://www.youtube.com/shorts/QExfdPPlzzs', 'https://www.youtube.com/shorts/QExfdPPlzzs', 'https://www.youtube.com/shorts/QbFZTnbOzp4', 'https://www.youtube.com/shorts/QbFZTnbOzp4', 'https://www.youtube.com/shorts/naQFPdjfmX4', 'https://www.youtube.com/shorts/naQFPdjfmX4', 'https://www.youtube.com/shorts/lsktN9Lh1_4', 'https://www.youtube.com/shorts/lsktN9Lh1_4', 'https://www.youtube.com/shorts/Q_M2HNBDNIE', 'https://www.youtube.com/shorts/Q_M2HNBDNIE']


download_folder = 'CenatUniverse'  # Customize your download folder
download_videos(video_urls, download_folder)