import PySimpleGUI as sg
import shutil
import os
import json

# Caminho para a pasta do desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Caminho para o arquivo JSON
caminho_arquivo = r'uteis\Games\OSU\GeradorDeMapa\config.json'


# Acesso ao arquivo JSON
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Nome da chave
pasta = "mapas_path"
audio = "audio_path"


# Valor da chave
valor_pasta = dados[pasta]
valor_audio = dados[audio]

if valor_pasta == "":
    valor_pasta = desktop_path



# tema da janela
sg.theme("Darkblack1")

quantidades = 1

# =========================================================================
#
#                           JANELA  
#
# =========================================================================



dificults = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]


if quantidades > len(dificults):
    for i in range(quantidades - (len(dificults))):
        dificults.append("~em branco~")
else:
    for i in range(len(dificults) - quantidades):
        dificults.pop(-1)
# Seleção de pasta
layoutPasta = [
        [sg.Text(valor_pasta, visible=True, key="caminhoPasta", justification="center")],
        [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path)], [sg.Button("Atualizar caminho da pasta", key="atualizarPasta")]
        ]

# Layout para a seleção de audio
layoutAudio = [
    [sg.Text(valor_audio, visible=True, key="caminhoAudio", justification="center")],
    [sg.FileBrowse("Procurar audio", key="audio", initial_folder=desktop_path)], [sg.Button("Mostrar caminho do audio", key="atualizarAudio")]
]
configMapas = [
        [sg.FilesBrowse("Biblioteca de sprites", key="sprites")],
        [sg.Frame("Seleção de pasta", layoutPasta)],
        [sg.Frame("Seleção de audio", layoutAudio)],
        [sg.Text("Quantidade de mapas"), sg.Input(key="quantidadeDificuldades", default_text=quantidades)]
        ]


configEditor = [
    [sg.Text("Dificuldade"), sg.Combo(dificults)],
    [sg.Text("Multiplicador de distância do snap"), sg.Input("3", key="distancesnap")],
    [sg.Text("Divisor do beat snap"), sg.Input("16")],
    [sg.Text("Tamanho da malha do editor"), sg.Input("4")],
    [sg.Text("Zoom da timeline"), sg.Input("4")],

]
configMetadata =[
    [sg.Text("Dificuldade"), sg.Combo(dificults)],
    [sg.Text("Título"), sg.Input(key="tittle")],
    [sg.Text("Título unicode"), sg.Input(key="unicodeTittle"),],
    [sg.Text("Artista"), sg.Input(key="artist"),],
    [sg.Text("Artista unicode"), sg.Input(key="unicodeArtist"),],
    [sg.Text("Criador"), sg.Input(key="creator"),],
    [sg.Text("Fonte"), sg.Input(key="source", )],
    [sg.Text("Etiquetas"), sg.Input(key="tags"),],
    [sg.Text("contagem (3,2,1)"), sg.Checkbox("", key="countdown")],
    [sg.Text("Tipo de click"), sg.Combo(("Normal", "Soft", "Drum"), key="sampleset")],
]

configDificulty = [
    [sg.Frame("Dificuldades", [
        [sg.Text("Dificuldade"), sg.Combo(dificults)],
        [sg.Text("HP"), sg.Input(key="hp")],
        [sg.Text("CS"), sg.Input(key="cs")],
        [sg.Text("OD"), sg.Input(key="od")],
        [sg.Text("AR"), sg.Input(key="ar")],
        ])]
]

configStoryboards = [
    [sg.Check("Storyboard background", key="bgstoryboard")],
    [sg.Check("Storyboard Fail", key="failstoryboard")],
    [sg.Check("Storyboard Pass", key="storyboardpass")],
    [sg.Check("Storyboard Foreground", key="storyboardfore")],
    [sg.Check("Storyboard Overlay", key="storyboardover")],

]

configAvançado = [
    [sg.Text("Dificuldade"), sg.Combo(dificults)],
    [sg.Text("Audio lead-in"), sg.Input("", key="audioleadin")],
    [sg.HorizontalSeparator()],
    [sg.Frame("Storyboards", configStoryboards)]
]
layout = [
    [sg.TabGroup([
        [sg.Tab("Arquivo",configMapas)],
        [sg.Tab("Metadata", configMetadata)],
        [sg.Tab("Dificuldade", configDificulty)],
        [sg.Tab("Editor", configEditor)],
        [sg.Tab("Avançado", configAvançado)],
    ])],
    [sg.Ok(), sg.Cancel("Cancelar")],
]

window = sg.Window("Configuração dos mapas", layout=layout)


while True:
    event, value = window.read()
    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break
    if event == "Ok":
        break
