import PySimpleGUI as sg
import youtube_dl
import os

# criar a pasta
def criar_pasta_destino(destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

#baixar vídeo
def baixar_video(link, destino):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

#baixar apenas o áudio
def baixar_audio(link, destino):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Layout da interface gráfica
layout = [
    [sg.Text('1. Baixar vídeo do YouTube')],
    [sg.Text('Link do vídeo:'), sg.InputText(key='link_video')],
    [sg.Button('Baixar Vídeo')],
    [sg.Text('2. Baixar vários vídeos do YouTube a partir de um arquivo .txt')],
    [sg.Text('Arquivo .txt com os links:'), sg.InputText(key='arquivo_txt')],
    [sg.Button('Baixar Vídeos')],
    [sg.Text('3. Baixar apenas áudio do YouTube')],
    [sg.Text('Link do vídeo:'), sg.InputText(key='link_audio')],
    [sg.Button('Baixar Áudio')],
    [sg.Text('4. Baixar apenas áudio de vários vídeos a partir de um arquivo .txt')],
    [sg.Text('Arquivo .txt com os links:'), sg.InputText(key='arquivo_txt_audio')],
    [sg.Button('Baixar Áudios')],
    [sg.Text('5. Acessar pasta de destino')],
    [sg.Button('Abrir Pasta de Destino')],
]

window = sg.Window('YouTube Downloader', layout)

# Loop para interagir com a interface gráfica
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    destino = 'C:\\Users\\fernando.silva8\\Desktop\\YouTubeDownloader'

    if event == 'Baixar Vídeo':
        link = values['link_video']
        criar_pasta_destino(destino)
        baixar_video(link, destino)

    if event == 'Baixar Vídeos':
        arquivo_txt = values['arquivo_txt']
        with open(arquivo_txt, 'r') as file:
            links = file.readlines()
        criar_pasta_destino(destino)
        for link in links:
            criar_pasta_destino(destino)
            baixar_video(link.strip(), destino)

    if event == 'Baixar Áudio':
        link = values['link_audio']
        criar_pasta_destino(destino)
        baixar_audio(link, destino)

    if event == 'Baixar Áudios':
        arquivo_txt = values['arquivo_txt_audio']
        with open(arquivo_txt, 'r') as file:
            links = file.readlines()
        criar_pasta_destino(destino)
        for link in links:
            criar_pasta_destino(destino)
            baixar_audio(link.strip(), destino)

    if event == 'Abrir Pasta de Destino':
        os.startfile(destino)

window.close()