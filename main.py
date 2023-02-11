# Here's an easy automated script for downloading YouTube videos.
# Simply use the code below to download any video without the need for any websites or apps.
from pytube import YouTube as yt
from pytube.exceptions import VideoUnavailable
import subprocess
import os

def download(url):
    try:
        video = yt(url)
    except VideoUnavailable:
        print(f'Video {url} is unavailable, skipping.')
        pass
    else:
        print(f'Downloading video: {video.title}')
        video.streams.get_by_itag(22).download()
        print('Video Downloaded!')
        subprocess.Popen(r'explorer ' + os.getcwd())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download(input('Youtube Video URL: '))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
