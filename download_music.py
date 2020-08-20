from youtube_search import YoutubeSearch
import youtube_dl

def download_music(music):
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'{music}.%(ext)s'
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    results = YoutubeSearch(music + '가사', max_results=1).to_dict()
    ydl.download(["https://www.youtube.com" + results[0]['url_suffix']])
    return f'{music}.mp3'

if __name__ == "__main__":
    pass