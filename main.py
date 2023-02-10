# Here's an easy automated script for downloading YouTube videos.
# Simply use the code below to download any video without the need for any websites or apps.
import pytube

def download(link):
    video_download = pytube.Youtube(link)
    video_download.streams.first().download()
    print('Video Downloaded', link)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download(input('Youtube Video URL: '))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
