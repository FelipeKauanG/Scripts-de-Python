import PySimpleGUIQt as sg
import os
import json
import screeninfo
import pygame

print("")
screenHeight = int(str(str(screeninfo.get_monitors()[0]).split(",")[3]).split("=")[1])
screenWidth = int(str(str(screeninfo.get_monitors()[0]).split(",")[2]).split("=")[1])



# Caminho para a pasta do desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Caminho para o arquivo JSON
caminhoArquivo = r'uteis\Games\OSU\GeradorDeMapa\config.json'


# Acesso ao arquivo JSON
with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Nome da chave
pasta = "mapas_path"
audio = "audio_path"
click_audio = "Audios"

fyletypesAudio = [
    ("Arquivos de áudio", "*.mp3"),
    ("Arquivos de áudio", "*.ogg"),
    ("Todos os arquivos", "*.*")
]
fyletypesSprites = [
    ("Arquivos de imagem", "*.png;*.jpg")
    ]

# Valor da chave
valor_pasta = dados[pasta]
valor_audio = dados[audio]
click = dados[click_audio]["Click"]["Audio"]

print(click)
def tocarSomClick():
    pygame.mixer.init()
    pygame.mixer_music.set_volume(0.1)
    pygame.mixer.music.load(click)
    pygame.mixer.music.play()

def Cancelar():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load(click)
    pygame.mixer.music.play()

if valor_pasta == "":
    valor_pasta = desktop_path


with open(r"uteis\Games\OSU\GeradorDeMapa\config.json", mode="r",
encoding="UTF-8") as arquivo:
    quantidades = json.load(arquivo)["Quantidade"]
    quantidades = int(quantidades)

# =========================================================================
#
#                               APLICATIVO
#
# =========================================================================

def Aplicativo():

    dificults = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]
    dificultsDefault = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]

    # Modifica a quantidade de dificuldades no array dificults
    def modfied(x=quantidades):
        if x > len(dificults):
            dificults.clear()
            
            for dif in dificultsDefault:
                dificults.append(dif)

            for i in range(x - (len(dificults))):
                dificults.append("~em branco~")

        else:
            for i in range(len(dificults) - x):
                dificults.pop(-1)
    # Seleção de pasta
    modfied()
    layoutPasta = [
            [sg.Text(valor_pasta, key="caminhoPasta", justification="center")],
            [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path, enable_events=True)]
            ]

    # Layout para a seleção de audio
    layoutAudio = [
        [sg.Text(valor_audio,  key="caminhoAudio", justification="center")],
        [sg.FileBrowse("Procurar audio", key="audio",
        initial_folder=desktop_path, file_types=fyletypesAudio, enable_events=True)]
    ]
    configMapas = [
            [sg.FilesBrowse("Biblioteca de sprites", key="sprites",
            enable_events=True, initial_folder=desktop_path,
            file_types=fyletypesSprites)],
            [sg.Frame("Seleção de pasta", layoutPasta, frame_color="#281259", background_color="#4B3084")],
            [sg.Frame("Seleção de audio", layoutAudio, frame_color="#281259", background_color="#4B3084")],
            [sg.Text("Quantidade de mapas", background_color="#4B3084")],
            [sg.Spin(values=[str(i) for i in range(1, 101)],
            key="quantidadeDificuldades", enable_events=True,
            initial_value=str(quantidades), background_color="#1E1C1B",text_color="#ffffff")],
            [sg.Button("?", enable_events=True, key="Qquantidade", )]
            ]


    configEditor = [
        [sg.Text("Dificuldade", background_color="#4b3084"), sg.Combo(dificults, enable_events=True, key="EDITOR", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Multiplicador de distância do snap", background_color="#4b3084"), sg.Input("3", key="distancesnap", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Divisor do beat snap", background_color="#4b3084"), sg.Input("16", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Tamanho da malha do editor", background_color="#4b3084"), sg.Input("4", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Zoom da timeline", background_color="#4b3084"), sg.Input("4", background_color="#1E1C1B", text_color="#ffffff")],

    ]
    configMetadata =[
        [sg.Text("Dificuldade", background_color="#4B3084"), sg.Combo(dificults, enable_events=True, key="METADATA", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Título", background_color="#4B3084"), sg.Input(key="tittle", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Título unicode", background_color="#4B3084"), sg.Input(key="unicodeTittle", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Artista", background_color="#4B3084"), sg.Input(key="artist", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Artista unicode", background_color="#4B3084"), sg.Input(key="unicodeArtist", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Criador", background_color="#4B3084"), sg.Input(key="creator", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Fonte", background_color="#4B3084"), sg.Input(key="source", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Etiquetas", background_color="#4B3084"), sg.Input(key="tags", background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("contagem (3,2,1)", background_color="#4B3084"), sg.Checkbox("", key="countdown", background_color="")],

        [sg.Text("Tipo de click", background_color="#4B3084"), sg.Combo(("Normal", "Soft", "Drum"), key="sampleset", background_color="#1E1C1B", text_color="#ffffff")]
    ]

    configDificulty = [
        [sg.Frame("", [
            [sg.Text("Dificuldade", background_color="#4b3084"), sg.Combo(dificults, enable_events=True, key="DIFICULDADE", background_color="#1E1C1B", text_color="#ffffff")],
            [sg.Text("HP", background_color="#4b3084"), sg.Input(key="hp", background_color="#1E1C1B", text_color="#ffffff")],
            [sg.Text("CS", background_color="#4b3084"), sg.Input(key="cs", background_color="#1E1C1B", text_color="#ffffff")],
            [sg.Text("OD", background_color="#4b3084"), sg.Input(key="od", background_color="#1E1C1B", text_color="#ffffff")],
            [sg.Text("AR", background_color="#4b3084"), sg.Input(key="ar", background_color="#1E1C1B", text_color="#ffffff")],
            ], frame_color="#281259", background_color="")]
    ]

    configStoryboards = [
        [sg.Check("Storyboard background", key="bgstoryboard", background_color="")],
        [sg.Check("Storyboard Fail", key="failstoryboard", background_color="")],
        [sg.Check("Storyboard Pass", key="storyboardpass", background_color="")],
        [sg.Check("Storyboard Foreground", key="storyboardfore", background_color="")],
        [sg.Check("Storyboard Overlay", key="storyboardover", background_color="")],

    ]

    configAvançado = [
        [sg.Text("Dificuldade", background_color="#4b3084"), sg.Combo(dificults, enable_events=True, key="AVANCADO", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Audio lead-in", background_color="#4b3084"), sg.Spin(values=[str(i) for i in range(1, 100)], key="audioleadin", initial_value=str(1), background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Frame("", configStoryboards, background_color="#4b3084")]
    ]
    layout = [
        [sg.Text("osu file format v14",pad=(5, 20))],
        [sg.TabGroup([
            [sg.Tab("Arquivo",configMapas, background_color="#070926")],
            [sg.Tab("Metadata", configMetadata, background_color="#070926")],
            [sg.Tab("Dificuldade", configDificulty, background_color="#070926")],
            [sg.Tab("Editor", configEditor, background_color="#070926")],
            [sg.Tab("Avançado", configAvançado, background_color="#070926")]], title_color="#ff0000", enable_events=True, key="Tab")],
        [sg.Ok(), sg.Cancel("Cancelar")]
    ]

    # Configuração da janela

    window = sg.Window("Configuração dos mapas",
            layout=layout, finalize=True,
            icon=r"uteis\Games\OSU\Icon.ico",
            background_color="#070926",
            size=(screenWidth*0.6, screenHeight*0.5
            ),location=(screenHeight*0.25, screenHeight*0.25)
            )

    while True:
        event, value = window.read()
        if event == "Cancelar" or event == sg.WIN_CLOSED:
            break
        if event == "Ok":
            print("\033[35m" + "Gerando mapa..." + "\033[m")
            break
        if event == "METADATA":
            True

        elif event == "DIFICULDADE":
            True

        elif event == "EDITOR":
            True

        elif event == "AVANCADO":
            True

        elif event == "audio": #Atualizar o caminho do audio
            if value["audio"][0] != "":
                print(f"Audio: {value["audio"][0]}")
                window["caminhoAudio"].update(value["audio"][0])

                with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    dados[audio] = value["audio"][0]

                with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        elif event == "pasta": #Atualiza o caminho da pasta
            if value["pasta"] != "":
                print(f"Pasta: {value["pasta"]}")
                window["caminhoPasta"].update(value["pasta"])
                with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    dados[pasta] = value["pasta"]
                    

                with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        elif event == "quantidadeDificuldades":
            try:
                valorQuantidade = value["quantidadeDificuldades"]
                valorQuantidade = int(valorQuantidade)

                with open(r"uteis\Games\OSU\GeradorDeMapa\config.json", encoding="UTF-8", mode="r") as arquivo:
                    dados = json.load(arquivo)

                with open(r"uteis\Games\OSU\GeradorDeMapa\config.json",encoding="UTF-8", mode="w") as arquivo:
                    dados["Quantidade"] = valorQuantidade
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                    modfied(valorQuantidade)
                    window["EDITOR"].update(values=dificults)
                    window["METADATA"].update(values=dificults)
                    window["DIFICULDADE"].update(values=dificults)
                    window["AVANCADO"].update(values=dificults)

            except ValueError:
                if valorQuantidade == "":
                    continue
                else:
                    [sg.popup("Por favor, digite apenas números inteiros")]
        elif event == "Qquantidade":
            [sg.popup("Essa lacuna representa a quantidade de mapas que você vai gerar\n\nSó não vai exaGERAR em ?")]
        else:
            tocarSomClick()
    window.close()
Aplicativo()
