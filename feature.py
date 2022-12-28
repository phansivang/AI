from pytube import YouTube


def download_youtube_video(link):
    youtubeObject = YouTube(link)

    try:
        youtubeObject.streams.get_by_resolution('720p').download()
    except:
        return 'An error has occurred'
    return 'Download is completed successfully'
