import PySimpleGUIQt as sg
import os
import json
import screeninfo
import pygame
import shutil
from numpy import arange


screenHeight = int(str(str(screeninfo.get_monitors()[0]).split(",")[3]).split("=")[1])
screenWidth = int(str(str(screeninfo.get_monitors()[0]).split(",")[2]).split("=")[1])

user = os.environ['USERPROFILE']
name_user = os.getlogin()

# Caminho para a pasta do desktop
desktop_path = os.path.join(os.path.join(user), 'Desktop')


preto = "#111111"
cinza = "#4f4f4f"
branco = "#eeeeee"
vermelho = "#ff4551"
verde = "#80ff4a"
azul = "#3342B7"
roxo = "#040823" #mediano
roxo1 = "#090130" #escuro
roxo2 = "#2B0F89" #claro
roxo3 = "#4829cf" #claro+
marrom = "#1E1C1B" #Escuro

fonte12 = "Calibri 12"
fonte14 = "Calibri 14"
fonte16 = "Calibri 16"


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
    click1 = dados[click_audio]["Click1"]["Audio"]
    Digitar = dados[click_audio]["Digitar"]["Audio"]
    erase = dados[click_audio]["Erase"]["Audio"]
    FailAplicar = dados[click_audio]["FailAplicar"]["Audio"]
    passAplicar = dados[click_audio]["AplicarPass"]["Audio"]

    if valor_pasta == "" or type(valor_pasta) == "<class 'NoneType'>":

        valor_pasta = desktop_path
        
        with open(caminhoArquivo, "w", encoding="UTF-8") as arquivo:
            dados["mapas_path"] = desktop_path
            print(f"Desktop path: {desktop_path}")
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    if type(valor_pasta) == "<class 'NoneType'>" or valor_audio == "":

        valor_audio = desktop_path 
        
        with open(caminhoArquivo, "w", encoding="UTF-8") as arquivo:
            dados["audio_path"] = desktop_path
            print(f"Desktop path: {desktop_path}")
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    print(valor_pasta)
    fyletypesAudio = [
        ("Arquivos de áudio", "*.mp3"),
        ("Arquivos de áudio", "*.ogg"),
        ("Todos os arquivos", "*.*")
    ]
    fyletypesSprites = [
        ("Arquivos de imagem", "*.png;*.jpg")
        ]

    def tocarSomclick1():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(click1)
        pygame.mixer.music.play()
    
    def tocarSomDigitando():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(Digitar)
        pygame.mixer.music.play()

    def EraseSound():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(erase)
        pygame.mixer.music.play()

    def FailAplicarSound():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(FailAplicar)
        pygame.mixer.music.play()

    def Aplicarpass():
        pygame.mixer.init()
        pygame.mixer_music.set_volume(0.1)
        pygame.mixer.music.load(passAplicar)
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
            [sg.Text(valor_pasta, key="caminhoPasta", justification="center", background_color=roxo, font=fonte14)],
            [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path, enable_events=True, font=fonte16, button_color=(branco, roxo3))]
            ]

    # Layout para a seleção de audio
    layoutAudio = [
        [sg.Text(valor_audio,  key="caminhoAudio", justification="center", background_color=roxo, font=fonte14)],
        [sg.FileBrowse("Procurar audio", key="audio",
        initial_folder=desktop_path, file_types=fyletypesAudio, enable_events=True, font=fonte16, button_color=(branco, roxo3))]
    ]
    configMapas = [
            [sg.FilesBrowse("Biblioteca de sprites", key="sprites",
            enable_events=True, initial_folder=desktop_path,
            file_types=fyletypesSprites, font=fonte16, button_color=(branco, roxo3))],
            [sg.Frame("Seleção de pasta", layoutPasta, frame_color="#281259", background_color=roxo2, font=fonte16)],
            [sg.Frame("Seleção de audio", layoutAudio, frame_color="#281259", background_color=roxo2, font=fonte16)],
            [sg.Text("Quantidade de mapas", background_color=roxo2, font=fonte16), sg.Button("?", enable_events=True, key="Qquantidade", font=fonte16,size=(4,1), button_color=(branco, cinza))],
            [sg.Spin(values=[str(i) for i in range(1, 101)],
            key="quantidadeDificuldades", enable_events=True,
            initial_value=str(quantidades), background_color=marrom,text_color="#ffffff", font=fonte16)]
            ]

    configMetadata =[
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16), sg.Combo(dificults, enable_events=True, key="METADATA", background_color=marrom, text_color="#ffffff")],
        [sg.Text("Título", background_color=roxo2, font=fonte16), sg.Input(key="tittle", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Título unicode", background_color=roxo2, font=fonte16), sg.Input(key="unicodeTittle", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Artista", background_color=roxo2, font=fonte16), sg.Input(key="artist", background_color=marrom, text_color="#ffffff", enable_events=True)],
        [sg.Text("Artista unicode", background_color=roxo2, font=fonte16), sg.Input(key="unicodeArtist", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Criador", background_color=roxo2, font=fonte16), sg.Input(key="creator", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Fonte", background_color=roxo2, font=fonte16), sg.Input(key="source", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Etiquetas", background_color=roxo2, font=fonte16), sg.Input(key="tags", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("contagem (3,2,1)", background_color=roxo2, font=fonte16), sg.Checkbox("", key="countdown", background_color="", enable_events=True)],
        

        [sg.Button("Aplicar", size=(25, 1), button_color=(branco, azul), font="Calibri 12 bold", enable_events=True, key="ConfigMetadata"), sg.Button("Limpar", size=(25, 1), button_color=(branco, cinza), font="Calibri 12 bold", enable_events=True, key="ConfigMetadataLimpar")]
    ]

    valueDificulty = arange(10, 0, step=-1)

    configDificulty = [
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16), sg.Combo(dificults, enable_events=True, key="DIFICULDADE", background_color=marrom, text_color="#ffffff")],
        [sg.Text("HP", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="hp", background_color=marrom, text_color="#ffffff", default_value=5)],
        [sg.Text("CS", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="cs", background_color=marrom, text_color="#ffffff", default_value=5)],
        [sg.Text("OD", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="od", background_color=marrom, text_color="#ffffff", default_value=5)],
        [sg.Text("AR", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="ar", background_color=marrom, text_color="#ffffff", default_value=5)],
        [sg.Button("Aplicar", size=(25, 1), button_color=(branco, azul), font="Calibri 12 bold", enable_events=True, key="ConfigDificulty")]
    ]
    configEditor = [
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16), sg.Combo(dificults, enable_events=True, key="EDITOR", background_color=marrom, text_color="#ffffff")],
        [sg.Text("Multiplicador de distância do snap", background_color=roxo2, font=fonte16), sg.Input("3", key="distancesnap", background_color=marrom, text_color="#ffffff", font=fonte16)],
        [sg.Text("Divisor do beat snap", background_color=roxo2, font=fonte16), sg.Input("16", background_color=marrom, text_color="#ffffff", font=fonte16)],
        [sg.Text("Tamanho da malha do editor", background_color=roxo2, font=fonte16), sg.Input("4", background_color=marrom, text_color="#ffffff", font=fonte16)],
        [sg.Text("Zoom da timeline", background_color=roxo2, font=fonte16), sg.Input("4", background_color=marrom, text_color="#ffffff", font=fonte16)],
        [sg.Button("Aplicar", size=(25,1), button_color=(branco, azul), font="Calibri 12 bold", enable_events=True, key="AplicarEditor")]

    ]


    configStoryboards = [
        [sg.Check("Storyboard background", key="bgstoryboard", background_color="", font=fonte16)],
        [sg.Check("Storyboard Fail", key="failstoryboard", background_color="", font=fonte16)],
        [sg.Check("Storyboard Pass", key="storyboardpass", background_color="", font=fonte16)],
        [sg.Check("Storyboard Foreground", key="storyboardfore", background_color="", font=fonte16)],
        [sg.Check("Storyboard Overlay", key="storyboardover", background_color="", font=fonte16)]
    ]
    configAvançado = [
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16),
        sg.Combo(dificults, enable_events=True, key="AVANCADO",
        background_color=marrom, text_color="#ffffff")],

        [sg.Text("Audio lead-in", background_color=roxo2, font="Calibri 16"),
        sg.Spin(values=[str(i) for i in range(1, 100)], key="audioleadin",
        initial_value=str(1), background_color=marrom, text_color="#ffffff",
        font="Calibri 14")],

        [sg.Frame("", configStoryboards, background_color=roxo2)],
        [sg.Button("Aplicar", size=(25,1), button_color=(branco, azul), font="Calibri 12 bold", enable_events=True, key="AplicarAvancado")]
    ]
    customização = [
        [sg.Check("Efeito sonoro de click", background_color=(roxo2), key="clickSound", font=fonte16)],

        [sg.Check("Efeito sonoro de modificação", background_color=(roxo2), key="ClickDigit", font=fonte16)],

        [sg.Check("Efeito sonoro de apagar", background_color=(roxo2), key="EraseSound", font=fonte16)],

        [sg.Check("Efeito sonoro de erro ao Aplicar", background_color=(roxo2), key="FailSound", font=fonte16)],

        [sg.Check("Efeito sonoro de Aplicar", background_color=(roxo2), key="AplicarSound", font=fonte16 )],

    ]
    layout = [
        [sg.Text(f"Seja bem vindo {name_user}\n",
            background_color="", font="Calibri 20 italic", text_color="#8253e6",
            enable_events=False)],
        [sg.TabGroup([

            [sg.Tab("Arquivo",configMapas, background_color=roxo1, key="Arquivo")],

            [sg.Tab("Metadata", configMetadata, background_color=roxo1, key="Metadata")],

            [sg.Tab("Dificuldade", configDificulty, background_color=roxo1, key="Dificuldade")],

            [sg.Tab("Editor", configEditor, background_color=roxo1, key="Editor")],

            [sg.Tab("Avançado", configAvançado, background_color=roxo1, key="Avançado")], 
            [sg.Tab("Personalizar", layout=customização, background_color=roxo1, key="custom")]
            ], enable_events=True, key="Tab")],


        [sg.Ok("Gerar mapas", size=(25,1), button_color=(preto, verde), font="Calibri 12 bold"), sg.Cancel("Cancelar", size=(25,1), button_color=(preto, vermelho), font="Calibri 12 bold")]
    ]

    # Configuração da janela

    window = sg.Window("Configuração dos mapas",
            layout=layout, finalize=True,
            icon=r"uteis/Games/OSU/Icon.ico",
            background_color=(roxo),
            size=(screenWidth*0.6, screenHeight*0.5),
            location=(screenHeight*0.25, screenHeight*0.25),
            element_justification="c",
            resizable=True,
            text_justification="c",
            border_depth="2",)


    # Formularios
    dificuldadeMETADATA = dificults[0]
    Titulo = ""
    TituloUnicode = ""
    Artista = ""
    ArtistaUnicode = ""
    Criador = ""
    Fonte = ""
    Etiquetas = ""
    Contagem = False
    Tipoclick1 = ""
    
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
                print("\033[36mGerando mapa\033[m")
        elif event == "pasta": #Atualiza o caminho da pasta
            caminho_pasta = value["pasta"]   
            if isinstance(caminho_pasta, str):
                print(f"\033[32m{caminho_pasta, type(caminho_pasta)}\033[m")
                valor_pasta = caminho_pasta
                window["caminhoPasta"].update(caminho_pasta)
                with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    dados[pasta] = caminho_pasta
                with open(caminhoArquivo, "w", encoding="UTF-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            else:
                print(f"\033[31m{caminho_pasta, type(caminho_pasta)}\033[m")

        elif event == "audio": #Atualizar o caminho do audio
            caminho_audio = value["audio"][0]
            valor_audio = caminho_audio

            if isinstance(caminho_audio, str) and caminho_audio != "":
                try:
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
            tocarSomclick1()
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
            except ValueError:
                if valorQuantidade == "":
                    continue
                else:
                    [sg.popup("Por favor, digite apenas números inteiros")]
        elif event == "Qquantidade":
            [sg.popup("Essa lacuna representa a quantidade de mapas que você vai gerar.\nSó não vai exaGERAR em ?")]

        elif event == "METADATA":
            tocarSomDigitando()
            dificuldadeMETADATA = value["METADATA"]
            print(dificuldadeMETADATA)
        elif event == "tittle":

            Titulo = value["tittle"]
            if value["tittle"] != "":
                tocarSomDigitando()
            #print(f"Titulo: {Titulo}")
        
        elif event == "unicodeTittle":
            TituloUnicode = value["unicodeTittle"]
            if TituloUnicode != "":
                tocarSomDigitando()
            #print(f"Titulo Unicode: {TituloUnicode}")
        
        elif event == "artist":
            Artista = value["artist"]
            if Artista != "":
                tocarSomDigitando()
            #print(f"Artista: {Artista}")
        
        elif event == "unicodeArtist":
            ArtistaUnicode = value["unicodeArtist"]
            if ArtistaUnicode != "":
                tocarSomDigitando()
        
        elif event == "creator":
            Criador = value["creator"]
            if Criador != "":
                tocarSomDigitando()
            #print(f"Criador: {Criador}")
        
        elif event == "source":
            Fonte = value["source"]
            if Fonte != "":
                tocarSomDigitando()
            #print(f"Fonte: {Fonte}")
        
        elif event == "tags":
            Etiquetas = value["tags"]
            if Etiquetas != "":
                tocarSomDigitando()
            #print(f"Etiquetas: {Etiquetas}")
        
        elif event == "countdown":
            Contagem = value["countdown"]
            if Contagem == True:
                print("Contagem ativada")
                Contagem = True
            else:
                print("Contagem desativada")
                Contagem = False
        
        elif event == "ConfigMetadata": # aplicar()
            

           
            Aplicarpass()
            mapaPronto = {
                "Dificuldade": f"{dificuldadeMETADATA}",
                "General": {
                    "AudioFilename": valor_audio,
                    "AudioLeadIn": 0,
                    "PreviewTime": 0,
                    "Countdown": Contagem,
                    "StackLeniency": 0.7,
                    "Mode": 0,
                    "LetterboxInBreaks": 0,
                    "widescreenStoryboard": 0
            },
                "Editor": {
                    "Bookmarks": [],
                    "DistanceSpacing": 0,
                    "BeatDivisor": 4,
                    "GridSize": 4,
                    "TimelineZoom": 1.4
            },
                "Metadata": {
                    "Title": Titulo,
                    "TitleUnicode": TituloUnicode,
                    "Artist": Artista,
                    "ArtistUnicode": ArtistaUnicode,
                    "Creator": Criador,
                    "Version": dificuldadeMETADATA,
                    "Source": Fonte,
                    "Tags": Etiquetas
            },
                "Difficulty": {
                    "HPDrainRate": 5,
                    "CircleSize": 5,
                    "OverallDifficulty": 5,
                    "ApproachRate": 5,
                    "SliderMultiplier": 1.4,
                    "SliderTickRate": 1
            }
            }
            print(mapaPronto)
            match Titulo:
                case "":
                    window["tittle"].update(background_color=vermelho)
                case _:
                    window["tittle"].update(background_color=marrom)
                    

            match TituloUnicode:
                case "":
                    window["unicodeTittle"].update(background_color=vermelho)
                case _:
                    window["unicodeTittle"].update(background_color=marrom)

            match Artista:
                case "":
                    window["artist"].update(background_color=vermelho)
                case _:
                    window["artist"].update(background_color=marrom)

            match ArtistaUnicode:
                case "":
                    window["unicodeArtist"].update(background_color=vermelho)
                case _:
                    window["unicodeArtist"].update(background_color=marrom)

            match Criador:
                case "":
                    window["creator"].update(background_color=vermelho)
                case _:
                    window["creator"].update(background_color=marrom)

            match Fonte:
                case "":
                    window["source"].update(background_color=vermelho)
                case _:
                    window["source"].update(background_color=marrom)

            match Etiquetas:
                case "":
                    window["tags"].update(background_color=vermelho)
                case _:
                    window["tags"].update(background_color=marrom)

            
            print((Titulo, TituloUnicode, Artista, ArtistaUnicode, Criador, Fonte, Etiquetas))

            if Titulo == "" or TituloUnicode == "" or Artista == "" or ArtistaUnicode == "" or Criador == "" or Fonte == "" or Etiquetas == "":
                [sg.popup("Preencha todos os campos por gentileza", background_color=roxo1, font=fonte12, button_color=(branco, cinza))]
                FailAplicarSound()


        elif event == "ConfigMetadataLimpar":
            LimparMetadata = [sg.popup_ok_cancel("Você tem certeza que deseja limpar tudo ?", background_color=roxo1, font=fonte12, button_color=(branco, cinza))]

            match LimparMetadata:
                case ["OK"]:

                    Titulo = ""
                    TituloUnicode = ""
                    Artista = ""
                    ArtistaUnicode = ""
                    Criador = ""
                    Fonte = ""
                    Etiquetas = ""

                    window["tittle"].update(value="", background_color=marrom)
                    window["unicodeTittle"].update(value="", background_color=marrom)
                    window["artist"].update(value="", background_color=marrom)
                    window["unicodeArtist"].update(value="", background_color=marrom)
                    window["creator"].update(value="", background_color=marrom)
                    window["source"].update(value="", background_color=marrom)
                    window["tags"].update(value="", background_color=marrom)
                    

                    
                    print((Titulo, TituloUnicode, Artista, ArtistaUnicode, Criador, Fonte, Etiquetas))
                    

                case "Cancel":
                    continue
        elif event == "Tab":
            tocarSomclick1()
        else:
            print(event)
    window.close()
Aplicativo()
