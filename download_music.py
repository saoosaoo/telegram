from youtube_search import YoutubeSearch
import youtube_dl

def search_music(music):
    results = YoutubeSearch(music + '가사', max_results=1).to_dict()
    return "https://www.youtube.com" + results[0]['url_suffix']

def download_music(music, url):
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
    ydl.download([url])
    return f'{music}.mp3'

if __name__ == "__main__":
    pass