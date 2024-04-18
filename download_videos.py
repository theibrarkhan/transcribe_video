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
video_urls = ['https://www.youtube.com/shorts/UJKSMSkoQNM', 'https://www.youtube.com/shorts/UJKSMSkoQNM', 'https://www.youtube.com/shorts/a6qmL6p5iJ0', 'https://www.youtube.com/shorts/a6qmL6p5iJ0', 'https://www.youtube.com/shorts/2kvDuN9J--8', 'https://www.youtube.com/shorts/2kvDuN9J--8', 'https://www.youtube.com/shorts/C5OYrCl98So', 'https://www.youtube.com/shorts/C5OYrCl98So', 'https://www.youtube.com/shorts/qwRZRQ2RcwQ', 'https://www.youtube.com/shorts/qwRZRQ2RcwQ', 'https://www.youtube.com/shorts/FebOXyLvGYc', 'https://www.youtube.com/shorts/FebOXyLvGYc', 'https://www.youtube.com/shorts/UryDapo37G4', 'https://www.youtube.com/shorts/UryDapo37G4', 'https://www.youtube.com/shorts/GNIAf-CUuI0', 'https://www.youtube.com/shorts/GNIAf-CUuI0', 'https://www.youtube.com/shorts/FWF-rpkhtAY', 'https://www.youtube.com/shorts/FWF-rpkhtAY', 'https://www.youtube.com/shorts/-NTIYRhszqw', 'https://www.youtube.com/shorts/-NTIYRhszqw', 'https://www.youtube.com/shorts/6hADe4oRUYA', 'https://www.youtube.com/shorts/6hADe4oRUYA', 'https://www.youtube.com/shorts/e3-6q0Q1xKc', 'https://www.youtube.com/shorts/e3-6q0Q1xKc', 'https://www.youtube.com/shorts/jiBmAoPpSJA', 'https://www.youtube.com/shorts/jiBmAoPpSJA', 'https://www.youtube.com/shorts/CrGT5OBbp5o', 'https://www.youtube.com/shorts/CrGT5OBbp5o', 'https://www.youtube.com/shorts/vH7Z47E-0xs', 'https://www.youtube.com/shorts/vH7Z47E-0xs', 'https://www.youtube.com/shorts/DjMeH9eUewU', 'https://www.youtube.com/shorts/DjMeH9eUewU', 'https://www.youtube.com/shorts/qQNuFsqcpPQ', 'https://www.youtube.com/shorts/qQNuFsqcpPQ', 'https://www.youtube.com/shorts/nWT1rTM8Ex0', 'https://www.youtube.com/shorts/nWT1rTM8Ex0', 'https://www.youtube.com/shorts/0lmcGE26cP8', 'https://www.youtube.com/shorts/0lmcGE26cP8', 'https://www.youtube.com/shorts/mJQOHUaXsWg', 'https://www.youtube.com/shorts/mJQOHUaXsWg', 'https://www.youtube.com/shorts/PI3Ee8jd3Z8', 'https://www.youtube.com/shorts/PI3Ee8jd3Z8', 'https://www.youtube.com/shorts/sndhPNIsUeQ', 'https://www.youtube.com/shorts/sndhPNIsUeQ', 'https://www.youtube.com/shorts/8ZeYPtiHrqc', 'https://www.youtube.com/shorts/8ZeYPtiHrqc', 'https://www.youtube.com/shorts/OD7USGg_G18', 'https://www.youtube.com/shorts/OD7USGg_G18', 'https://www.youtube.com/shorts/VyRB9oXrQbA', 'https://www.youtube.com/shorts/VyRB9oXrQbA', 'https://www.youtube.com/shorts/9OT1H0NW6To', 'https://www.youtube.com/shorts/9OT1H0NW6To', 'https://www.youtube.com/shorts/VZdJ7VPbcaQ', 'https://www.youtube.com/shorts/VZdJ7VPbcaQ', 'https://www.youtube.com/shorts/MuHeLfxvdqA', 'https://www.youtube.com/shorts/MuHeLfxvdqA', 'https://www.youtube.com/shorts/3qXHnEPynrQ', 'https://www.youtube.com/shorts/3qXHnEPynrQ', 'https://www.youtube.com/shorts/ufMgxEe9Zso', 'https://www.youtube.com/shorts/ufMgxEe9Zso', 'https://www.youtube.com/shorts/A4Tekpx5CgE', 'https://www.youtube.com/shorts/A4Tekpx5CgE', 'https://www.youtube.com/shorts/4eLaYCoMJpc', 'https://www.youtube.com/shorts/4eLaYCoMJpc', 'https://www.youtube.com/shorts/hqAgAcSH6G4', 'https://www.youtube.com/shorts/hqAgAcSH6G4', 'https://www.youtube.com/shorts/mJ-gDBt5Fww', 'https://www.youtube.com/shorts/mJ-gDBt5Fww', 'https://www.youtube.com/shorts/ngL5f9fotRo', 'https://www.youtube.com/shorts/ngL5f9fotRo', 'https://www.youtube.com/shorts/3A4IlfQlkDI', 'https://www.youtube.com/shorts/3A4IlfQlkDI', 'https://www.youtube.com/shorts/dLsqBtcsu_g', 'https://www.youtube.com/shorts/dLsqBtcsu_g', 'https://www.youtube.com/shorts/M8jdWGzFXqI', 'https://www.youtube.com/shorts/M8jdWGzFXqI', 'https://www.youtube.com/shorts/_ygGsi9MQC0', 'https://www.youtube.com/shorts/_ygGsi9MQC0', 'https://www.youtube.com/shorts/NkeQJG7KqTc', 'https://www.youtube.com/shorts/NkeQJG7KqTc', 'https://www.youtube.com/shorts/sdCvj7ey6OI', 'https://www.youtube.com/shorts/sdCvj7ey6OI', 'https://www.youtube.com/shorts/cioPtoUklO8', 'https://www.youtube.com/shorts/cioPtoUklO8', 'https://www.youtube.com/shorts/6Roy8P4NkHU', 'https://www.youtube.com/shorts/6Roy8P4NkHU', 'https://www.youtube.com/shorts/CIDx_WBePQ8', 'https://www.youtube.com/shorts/CIDx_WBePQ8', 'https://www.youtube.com/shorts/y4Rtohmx5bQ', 'https://www.youtube.com/shorts/y4Rtohmx5bQ', 'https://www.youtube.com/shorts/4e-0NhgcFUc', 'https://www.youtube.com/shorts/4e-0NhgcFUc', 'https://www.youtube.com/shorts/JX2F7iCmoHs', 'https://www.youtube.com/shorts/JX2F7iCmoHs', 'https://www.youtube.com/shorts/-S01F1GmeLw', 'https://www.youtube.com/shorts/-S01F1GmeLw', 'https://www.youtube.com/shorts/l8n8CfreXQQ', 'https://www.youtube.com/shorts/l8n8CfreXQQ', 'https://www.youtube.com/shorts/6XqaqETL4tQ', 'https://www.youtube.com/shorts/6XqaqETL4tQ']


download_folder = 'Emiru'  # Customize your download folder
download_videos(video_urls, download_folder)