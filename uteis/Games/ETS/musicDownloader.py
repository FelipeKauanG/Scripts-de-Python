import os
import yt_dlp
import concurrent.futures

# Definindo as playlists
playlist_urls = [
    'https://www.youtube.com/playlist?list=PLQifnHLPvFjBfg_KQgghOz9yfufaZSAWC',
    'https://www.youtube.com/playlist?list=PLQifnHLPvFjB7Lkx2Ln9YksMYCsXqJs25',
    'https://www.youtube.com/playlist?list=PLQifnHLPvFjBEJHbOfL4zmRGTpJTFs-B-',
    'https://www.youtube.com/playlist?list=PLQifnHLPvFjDwvpmfUNZVD11jZIO8CYOJ'
]

output_dir = r'C:\Users\Shadic\Music'
os.makedirs(output_dir, exist_ok=True)

def get_video_urls_from_playlist(playlist_url):
    """Obtém todos os vídeos de uma playlist."""
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Extrai apenas as URLs dos vídeos, sem baixar os vídeos
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        if 'entries' in result:
            return [entry['url'] for entry in result['entries']]  # Retorna todas as URLs dos vídeos
        return []

def download_video(video_url):
    """Baixa um vídeo individualmente."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,  # Exibe as mensagens de erro e progresso
        'ignoreerrors': True,  # Ignora vídeos com erro
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Download do vídeo {video_url} concluído!")
        except Exception as e:
            print(f"Erro ao baixar o vídeo {video_url}: {e}")

# Coletando todos os vídeos de todas as playlists
all_video_urls = []
for playlist_url in playlist_urls:
    video_urls = get_video_urls_from_playlist(playlist_url)
    all_video_urls.extend(video_urls)

# Usando ThreadPoolExecutor para rodar os downloads simultaneamente
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download_video, all_video_urls)

print("🎵 Todos os downloads de vídeos concluídos.")
