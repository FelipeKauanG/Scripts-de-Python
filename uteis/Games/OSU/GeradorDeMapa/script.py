import PySimpleGUIQt as sg
import os
import json
import screeninfo
import pygame
import shutil
from numpy import arange
print(arange(1, 10))


screenHeight = int(str(str(screeninfo.get_monitors()[0]).split(",")[3]).split("=")[1])
screenWidth = int(str(str(screeninfo.get_monitors()[0]).split(",")[2]).split("=")[1])

user = os.environ['USERPROFILE']
name_user = os.getlogin()


sg.theme("Darkgrey14")
# Caminho para a pasta do desktop
desktop_path = os.path.join(os.path.join(user), 'Desktop')

Titulo = ""
TituloUnicode = ""
Artista = ""
ArtistaUnicode = ""
Criador = ""
Fonte = ""
Etiquetas = ""
Contagem = False
TipoClick = ""
def criarMapas(x):
    mapas = []
    for i in range(0, x):
        mapas.append("Aaaaaaa")
    print(mapas)

# APP
def Aplicativo():
    # Caminho para o arquivo JSON
    caminhoArquivo = f"C:/Users/{name_user}/Documents/GitHub/Scripts-de-Python/uteis/Games/OSU/GeradorDeMapa/config.json"
    # Acesso ao arquivo JSON
    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    # Nome da chave
    pasta = "mapas_path"
    audio = "audio_path"
    click_audio = "Audios"

    # Valor da chave
    valor_pasta = dados[pasta]
    valor_audio = dados[audio]
    click = dados[click_audio]["Click"]["Audio"]

    if valor_pasta == "" or valor_pasta == None:
        valor_pasta = desktop_path   
        with open(caminhoArquivo, "w", encoding="UTF-8") as arquivo:
            dados["mapas_path"] = desktop_path
            print(f"Desktop path: {desktop_path}")
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)


    fyletypesAudio = [
        ("Arquivos de áudio", "*.mp3"),
        ("Arquivos de áudio", "*.ogg"),
        ("Todos os arquivos", "*.*")
    ]
    fyletypesSprites = [
        ("Arquivos de imagem", "*.png;*.jpg")
        ]

    def tocarSomClick():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(click)
        pygame.mixer.music.play()


    with open(r"uteis/Games/OSU/GeradorDeMapa/config.json", mode="r",
    encoding="UTF-8") as arquivo:
        quantidades = json.load(arquivo)["Quantidade"]
        quantidades = int(quantidades)



    dificults = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]
    dificultsDefault = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]

    # Modifica a quantidade de dificuldades no array dificults
    def modfied(x=quantidades):
        if x > len(dificults):
            for i in range(x - (len(dificults))):
                dificults.append("~em branco~")
        else:
            for i in range(len(dificults) - x):
                dificults.pop(-1)
        for i in range(0, len(dificults)):
            if len(dificults) <= len(dificultsDefault):
                dificults[i] = dificultsDefault[i]

    # Seleção de pasta
    modfied()
    layoutPasta = [
            [sg.Text(valor_pasta, key="caminhoPasta", justification="center")],
            [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path, enable_events=True, font="Calibri 16")]
            ]

    # Layout para a seleção de audio
    layoutAudio = [
        [sg.Text(valor_audio,  key="caminhoAudio", justification="center")],
        [sg.FileBrowse("Procurar audio", key="audio",
        initial_folder=desktop_path, file_types=fyletypesAudio, enable_events=True, font="Calibri 16")]
    ]
    configMapas = [
            [sg.FilesBrowse("Biblioteca de sprites", key="sprites",
            enable_events=True, initial_folder=desktop_path,
            file_types=fyletypesSprites, font="Calibri 16")],
            [sg.Frame("Seleção de pasta", layoutPasta, frame_color="#281259", background_color="#4B3084")],
            [sg.Frame("Seleção de audio", layoutAudio, frame_color="#281259", background_color="#4B3084")],
            [sg.Text("Quantidade de mapas", background_color="#4B3084", font="Calibri 16")],
            [sg.Spin(values=[str(i) for i in range(1, 101)],
            key="quantidadeDificuldades", enable_events=True,
            initial_value=str(quantidades), background_color="#1E1C1B",text_color="#ffffff", font="Calibri 16")],
            [sg.Button("?", enable_events=True, key="Qquantidade", font="Calibri 16")]
            ]


    configEditor = [
        [sg.Text("Dificuldade", background_color="#4b3084", font="Calibri 16"), sg.Combo(dificults, enable_events=True,font="Calibri 16", key="EDITOR", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Multiplicador de distância do snap", background_color="#4b3084", font="Calibri 16"), sg.Input("3", key="distancesnap", background_color="#1E1C1B", text_color="#ffffff", font="Calibri 16")],
        [sg.Text("Divisor do beat snap", background_color="#4b3084", font="Calibri 16"), sg.Input("16", background_color="#1E1C1B", text_color="#ffffff", font="Calibri 16")],
        [sg.Text("Tamanho da malha do editor", background_color="#4b3084", font="Calibri 16"), sg.Input("4", background_color="#1E1C1B", text_color="#ffffff", font="Calibri 16")],
        [sg.Text("Zoom da timeline", background_color="#4b3084", font="Calibri 16"), sg.Input("4", background_color="#1E1C1B", text_color="#ffffff", font="Calibri 16")],

    ]
    configMetadata =[
        [sg.Text("Dificuldade", background_color="#4B3084", font="Calibri 16"), sg.Combo(dificults, enable_events=True, key="METADATA", background_color="#1E1C1B", text_color="#ffffff")],
        [sg.Text("Título", background_color="#4B3084", font="Calibri 16"), sg.Input(key="tittle", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Título unicode", background_color="#4B3084", font="Calibri 16"), sg.Input(key="unicodeTittle", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Artista", background_color="#4B3084", font="Calibri 16"), sg.Input(key="artist", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Artista unicode", background_color="#4B3084", font="Calibri 16"), sg.Input(key="unicodeArtist", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Criador", background_color="#4B3084", font="Calibri 16"), sg.Input(key="creator", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Fonte", background_color="#4B3084", font="Calibri 16"), sg.Input(key="source", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("Etiquetas", background_color="#4B3084", font="Calibri 16"), sg.Input(key="tags", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)],
        [sg.Text("contagem (3,2,1)", background_color="#4B3084", font="Calibri 16"), sg.Checkbox("", key="countdown", background_color="", enable_events=True)],
        [sg.Text("Tipo de click", background_color="#4B3084", font="Calibri 16"), sg.Combo(("Normal", "Soft", "Drum"), key="sampleset", background_color="#1E1C1B", text_color="#ffffff", enable_events=True)]
    ]
    valueDificulty = arange(10, 0, step=-1)
    configDificulty = [
        [sg.Frame("", [
            [sg.Text("Dificuldade", background_color="#4b3084", font="Calibri 16"), sg.Combo(dificults, enable_events=True, key="DIFICULDADE", background_color="#1E1C1B", text_color="#ffffff")],
            [sg.Text("HP", background_color="#4b3084", font="Calibri 16"), sg.Combo(values= (valueDificulty), key="hp", background_color="#1E1C1B", text_color="#ffffff", default_value=5)],
            [sg.Text("CS", background_color="#4b3084", font="Calibri 16"), sg.Combo(values= (valueDificulty), key="cs", background_color="#1E1C1B", text_color="#ffffff", default_value=5)],
            [sg.Text("OD", background_color="#4b3084", font="Calibri 16"), sg.Combo(values= (valueDificulty), key="od", background_color="#1E1C1B", text_color="#ffffff", default_value=5)],
            [sg.Text("AR", background_color="#4b3084", font="Calibri 16"), sg.Combo(values= (valueDificulty), key="ar", background_color="#1E1C1B", text_color="#ffffff", default_value=5)],
            ], frame_color="#281259", background_color="")]
    ]
    configStoryboards = [
        [sg.Check("Storyboard background", key="bgstoryboard", background_color="", font="Calibri 16")],
        [sg.Check("Storyboard Fail", key="failstoryboard", background_color="", font="Calibri 16")],
        [sg.Check("Storyboard Pass", key="storyboardpass", background_color="", font="Calibri 16")],
        [sg.Check("Storyboard Foreground", key="storyboardfore", background_color="", font="Calibri 16")],
        [sg.Check("Storyboard Overlay", key="storyboardover", background_color="", font="Calibri 16")],
    ]
    configAvançado = [
        [sg.Text("Dificuldade", background_color="#4b3084", font="Calibri 16"),
        sg.Combo(dificults, enable_events=True, key="AVANCADO",
        background_color="#1E1C1B", text_color="#ffffff")],

        [sg.Text("Audio lead-in", background_color="#4b3084", font="Calibri 16"),
        sg.Spin(values=[str(i) for i in range(1, 100)], key="audioleadin",
        initial_value=str(1), background_color="#1E1C1B", text_color="#ffffff",
        font="Calibri 14")],

        [sg.Frame("", configStoryboards, background_color="#4b3084")]
    ]

    layout = [
        [sg.TabGroup([

            [sg.Text(f"Seja bem vindo {name_user}",
            background_color="", font="Calibri 16 italic", text_color="#8253e6",
            enable_events=False)],

            [sg.Tab("Arquivo",configMapas, background_color="#070926", key="Arquivo")],

            [sg.Tab("Metadata", configMetadata, background_color="#070926", key="Metadata")],

            [sg.Tab("Dificuldade", configDificulty, background_color="#070926", key="Dificuldade")],

            [sg.Tab("Editor", configEditor, background_color="#070926", key="Editor")],

            [sg.Tab("Avançado", configAvançado, background_color="#070926", key="Avançado")]],

            enable_events=True, key="Tab")],
        [sg.Ok(), sg.Cancel("Cancelar")]
    ]

    # Configuração da janela

    window = sg.Window("Configuração dos mapas",
            layout=layout, finalize=True,
            icon=r"uteis/Games/OSU/Icon.ico",
            background_color="#070926",
            size=(screenWidth*0.6, screenHeight*0.5
            ),location=(screenHeight*0.25, screenHeight*0.25)
            )

    while True:
        event, value = window.read()
        if event == "Cancelar" or event == sg.WIN_CLOSED:
            break
        temMapa = 0
        if event == "Ok":
            for difi in dificults:
                if difi == "~em branco~":
                    temMapa +=1
            if temMapa == 1:
                [sg.popup(f"Existem {temMapa} mapa em branco")]
            elif temMapa > 1:
                [sg.popup(f"Existem {temMapa} mapas em branco")]
            else:
                print("/033[35m" + "Gerando mapa..." + "/033[m")
                
        elif event == "pasta": #Atualiza o caminho da pasta
            caminho_pasta = value["pasta"]
            if caminho_pasta != "":
                valor_pasta = caminho_pasta
                print(f"Pasta: {caminho_pasta}")
                window["caminhoPasta"].update(caminho_pasta)
                with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    dados[pasta] = caminho_pasta
                with open(caminhoArquivo, "w", encoding="UTF-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        elif event == "audio": #Atualizar o caminho do audio
            print(os.listdir(valor_pasta))
            caminho_audio = value["audio"][0]
            valor_audio = caminho_audio
            if caminho_audio != "":
                try:
                    print(f"Audio: {caminho_audio}")
                    window["caminhoAudio"].update(caminho_audio)
                    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        dados[audio] = caminho_audio

                    with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
                        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                    with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
                        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

                    shutil.copy(caminho_audio, valor_pasta)

                except shutil.SameFileError:
                    [sg.popup("Já existe esse audio na pasta")]
        elif event == "quantidadeDificuldades":
            try:
                valorQuantidade = value["quantidadeDificuldades"]
                valorQuantidade = int(valorQuantidade)
                with open(r"uteis/Games/OSU/GeradorDeMapa/config.json", encoding="UTF-8", mode="r") as arquivo:
                    dados = json.load(arquivo)

                with open(r"uteis/Games/OSU/GeradorDeMapa/config.json",encoding="UTF-8", mode="w") as arquivo:
                    dados["Quantidade"] = valorQuantidade
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                    modfied(valorQuantidade)
                    window["EDITOR"].update(values=dificults)
                    window["METADATA"].update(values=dificults)
                    window["DIFICULDADE"].update(values=dificults)
                    window["AVANCADO"].update(values=dificults)

                criarMapas(valorQuantidade)
            except ValueError:
                if valorQuantidade == "":
                    continue
                else:
                    [sg.popup("Por favor, digite apenas números inteiros")]
        elif event == "Qquantidade":
            [sg.popup("Essa lacuna representa a quantidade de mapas que você vai gerar.\nSó não vai exaGERAR em ?")]
        
        elif event == "Tab":
            print(value["Tab"])

        elif

        elif event == "tittle":
            Titulo = value["tittle"]

            print(Titulo)
        elif event == "unicodeTittle":
            TituloUnicode = value["unicodeTittle"]
            print(TituloUnicode)
        elif event == "artist":
            Artista = value["artist"]
            print(Artista)
        elif event == "unicodeArtist":
            ArtistaUnicode = value["unicodeArtist"]
            print(ArtistaUnicode)
        elif event == "creator":
            Criador = value["creator"]
            print(Criador)
        elif event == "source":
            Fonte = value["source"]
            print(Fonte)
        elif event == "tags":
            Etiquetas = value["tags"]
            print(Etiquetas)
        elif event == "countdown":
            Contagem = value["countdown"]
            if Contagem == True:
                print("Contagem ativada")
            else:
                print("Contagem desativada")
        elif event == "sampleset":
            TipoClick = value["sampleset"]
            if TipoClick == "Normal":
                print("Tipo de click: Normal")
            elif TipoClick == "Soft":
                print("Tipo de click: Soft")
            elif TipoClick == "Drum":
                print("Tipo de click: Drum")



        else:
            tocarSomClick()
            print(event)
    window.close()
Aplicativo()
