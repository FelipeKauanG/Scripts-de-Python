import PySimpleGUIQt as sg
import shutil
import os
import json

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')



# tema da janela
sg.theme("Dark")

# Seleção de pasta
layoutPasta = [
    [sg.Text("", visible=True, key="caminhoPasta", justification="center")],
    
    [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path)], [sg.Button("Mostrar caminho da pasta", key="atualizarPasta")]
    ]

# Layout para a seleção de audio
layoutAudio = [
    [sg.Text("", visible=True, key="caminhoAudio", justification="center")],
    [sg.FileBrowse("Procurar audio", key="audio", initial_folder=desktop_path)], [sg.Button("Mostrar caminho do audio", key="atualizarAudio")]
]

# Formulario principal da janela
formulario = [
    [sg.Text("Título"), sg.Input(key="tittle")],
    [sg.Text("Título unicode"), sg.Input(key="unicodeTittle"),],
    [sg.Text("Artista"), sg.Input(key="artist"),],
    [sg.Text("Artista unicode"), sg.Input(key="unicodeArtist"),],
    [sg.Text("Criador"), sg.Input(key="creator"),],
    [sg.Text("Fonte"), sg.Input(key="source", )],
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
reposta = "no"

window = sg.Window("Gerador de Mapa", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    if event == "atualizarPasta":
        window["caminhoPasta"].update(values["pasta"], visible=True)
    if event == "atualizarAudio":
        window["caminhoAudio"].update(values["audio"][0], visible=True)
    if event == "Ok":
        print()
        for nome in values:
            if not values["pasta"]:
                [sg.popup("Selecione uma pasta")]
                break
            
            if not values["quantidadeDificuldades"]:
                [sg.popup("Preencha o campo de quantidade de dificuldades por gentileza")]
                break
            
            elif values["quantidadeDificuldades"].isnumeric() == False:
                [sg.popup("Por favor, digite apenas números!")]
                break

            elif int(values["quantidadeDificuldades"]) < 1:
                [sg.popup("Por favor, digite apenas números positivos\nno campo de quantidade de dificuldades!")]
                break

            elif int(values["quantidadeDificuldades"]) > 10 and reposta == "no":

                evento = sg.popup_yes_no("Você tem certeza que deseja criar mais de 10 dificuldades?")

                if evento == "Yes":
                    reposta = "yes"
                    pass
                else:
                    values["quantidadeDificuldades"] = ""
                    break
                break

            if not values["audio"]:
                [sg.popup("Selecione um audio")]
                break
            if not values["tittle"]:
                [sg.popup("Digite um título")]
                break
            if not values["unicodeTittle"]:
                [sg.popup("Digite um título unicode")]
                break
            if not values["artist"]:
                [sg.popup("Digite um artista")]
                break
            if not values["unicodeArtist"]:
                [sg.popup("Digite um artista unicode")]
                break
            if not values["creator"]:
                [sg.popup("Digite um criador")]
                break
            if not values["source"]:
                [sg.popup("Digite uma fonte")]
                break   
            if not values["tags"]:
                [sg.popup("Digite etiquetas")]
                break    
            else:
                with open("config.json", "w") as file:
                    print(json.dump(values, file))
                break
    

print(formulario)

window.close()
