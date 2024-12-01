import PySimpleGUIQt as sg
import shutil
import os
import json

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# tema da janela
sg.theme("Dark")

# Seleção de pasta
layoutPasta = [
    [sg.Text("Caminho", visible=True, key="caminho", justification="center")],
    
    [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path)], [sg.Button("Selecionar", key="selecionarPasta")],

    ]

# Layout para a seleção de audio
layoutAudio = [
    [sg.FileBrowse("Procurar audio", key="audio", initial_folder=desktop_path)], [sg.Button("Selecionar")]
]

# Formulario principal da janela
formulario = [
    [sg.Text("Título"), sg.Input(key="tittle")],
    [sg.Text("Título unicode"), sg.Input(key="unicodeTittle"),],
    [sg.Text("Artista"), sg.Input(key="artist"),],
    [sg.Text("Artista unicode"), sg.Input(key="unicodeArtist"),],
    [sg.Text("Criador"), sg.Input(key="creator"),],
    [sg.Text("Fonte"), sg.Input(key="source"),],
    [sg.Text("Etiquetas"), sg.Input(key="tags"),]
]

# Layout do programa
layout = [
    [sg.Frame("Seleção de pasta", layoutPasta)],
    [sg.Text("Quantidade de dificuldades"), sg.Input(key="quantidadeDificuldades")],
    [sg.Frame("Seleção de audio", layoutAudio)],
    [sg.Frame("Formulário", formulario)],
    [sg.Ok(), sg.Cancel("Cancelar")]
    ]
    
window = sg.Window("Gerador de Mapa", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    if event == "Ok":
        print()
        for nome in values:
            print(nome, values[nome], end="\n")
window.close()
