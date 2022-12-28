from pytube import YouTube
import os

def download_youtube_video(link):
    youtubeObject = YouTube(link)

    try:
        youtubeObject.streams.get_by_resolution('720p').download(os.path.expanduser("~/Downloads"))
    except:
        return 'An error has occurred'
    return 'Download is completed successfully'
