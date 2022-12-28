from pytube import YouTube


def download_youtube_video(link):
    youtubeObject = YouTube(link)

    try:
        youtubeObject.streams.first()
        youtubeObject.streams.get_by_resolution('720p').download(output_path='/dev/null')
    except:
        return 'An error has occurred'
    return 'Download is completed successfully'
