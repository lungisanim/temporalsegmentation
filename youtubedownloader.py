from pytube import YouTube
import math, os, cv2
import ssl
import requests

import certifi
import ssl
context = ssl.create_default_context(cafile=certifi.where())

youtube_url = requests.get('https://www.youtube.com/watch?v=6rJndnVNMEY,5a4188d704be4c48b21754e5ee7f2b34', verify=True)
yt = YouTube(youtube_url)



stream = yt.streams.filter(file_extension='mp4').first()
download_path = stream.download()

if not os.path.exists(download_path):
    print('Error downloading video')
    exit(0)