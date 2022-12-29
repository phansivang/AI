from pytube import YouTube
import os

def download_youtube_video(link):
    youtubeObject = YouTube(link)

    try:

        youtube = youtubeObject.streams.first()
        youtube.download(output_path=os.path.expanduser("~/Downloads"))
        # youtubeObject.streams.get_by_resolution('720p').download(output_path='/dev/null')
    except:
        return 'An error has occurred'
    return 'Download is completed successfully'
