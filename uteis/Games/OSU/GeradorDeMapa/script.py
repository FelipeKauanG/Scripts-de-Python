import PySimpleGUIQt as sg
import os
import json
import screeninfo
import shutil
from numpy import arange
import zipfile


screenHeight = int(str(str(screeninfo.get_monitors()[0]).split(",")[3]).split("=")[1])
screenWidth = int(str(str(screeninfo.get_monitors()[0]).split(",")[2]).split("=")[1])

user = os.environ['USERPROFILE']
name_user = os.getlogin()

# Caminho para a pasta do desktop
desktop_path = os.path.join(os.path.join(user), 'Desktop')


preto = "#111111"
cinza = "#4f4f4f"
branco = "#eeeeee"
vermelho = "#ff4555"
verde = "#caff45"
azul = "#3342B7"
roxo = "#040823" #mediano
roxo1 = "#090130" #escuro
roxo2 = "#2B0F89" #claro
roxo3 = "#4829cf" #claro+
marrom = "#1E1C1B" #Escuro

fonte12 = "Calibri 12"
fonte14 = "Calibri 14"
fonte16 = "Calibri 16"

osu_blank_genrl = {
    "AudioFilename": "",
    "AudioLeadIn": 0,
    "PreviewTime":-1,
    "Countdown": 0,
    "SampleSet": "Normal",
    "StackLeniency": 0.7,
    "Mode": 0,
    "LetterboxInBreaks": 0,
    "WidescreenStoryboard": 0,
}

osu_blank_editor = {
    "DistanceSpacing": 1.3,
    "BeatDivisor": 4,
    "GridSize": 16,
    "TimelineZoom": 1
}

osu_blank_metadata = {
    "Title": "",
    "TitleUnicode": "",
    "Artist": "",
    "ArtistUnicode": "",
    "Creator": "",
    "Version": "",
    "Source": "",
    "Tags": "",
    "BeatmapID": 0,
    "BeatmapSetID": -1,
}

osu_blank_dificculty = {
    "HPDrainRate": 5,
    "CircleSize": 5,
    "OverallDifficulty": 5,
    "ApproachRate": 5,
    "SliderMultiplier": 1.4,
    "SliderTickRate": 1
}

osu_blank_events = (
    "//Background and Video vents",
    "//Break Periods",
    "//Storyboard layer 0 (Background)",
    "//Storyboard layer 1 (Fail)",
    "//Storyboard layer 2 (Pass)",
    "//Storyboard layer 3 (Foreground)",
    "//Storyboard layer 4 (Overlay)",
    "//Storyboard Sound Sample",
)


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

    # Valor da chave
    valor_pasta = dados[pasta]
    valor_audio = dados[audio]

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
            [sg.Spin(values=[str(i) for i in range(1, 101)],
            key="quantidadeDificuldades", enable_events=True,
            initial_value=str(quantidades), background_color=marrom,text_color="#ffffff", font=fonte16)]
            ]

    configMetadata =[
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16), sg.Combo(dificults, enable_events=True, key="METADATA", background_color=marrom, text_color="#ffffff", font=fonte12)],
        [sg.Text("Título", background_color=roxo2, font=fonte16), sg.Input(key="tittle", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Título unicode", background_color=roxo2, font=fonte16), sg.Input(key="unicodeTittle", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Artista", background_color=roxo2, font=fonte16), sg.Input(key="artist", background_color=marrom, text_color="#ffffff", enable_events=True)],
        [sg.Text("Artista unicode", background_color=roxo2, font=fonte16), sg.Input(key="unicodeArtist", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Criador", background_color=roxo2, font=fonte16), sg.Input(key="creator", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Fonte", background_color=roxo2, font=fonte16), sg.Input(key="source", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("Etiquetas", background_color=roxo2, font=fonte16), sg.Input(key="tags", background_color=marrom, text_color="#ffffff", enable_events=True, font=fonte12)],
        [sg.Text("contagem (3,2,1)", background_color=roxo2, font=fonte16), sg.Checkbox("", key="countdown", background_color="", enable_events=True)]
    ]

    valueDificulty = arange(10, 0, step=-1)

    configDificulty = [
        [sg.Text("Dificuldade", background_color=roxo2, font=fonte16), sg.Combo(dificults, enable_events=True, key="DIFICULDADE", background_color=marrom, text_color="#ffffff", font=fonte12)],
        [sg.Text("HP", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="hp", background_color=marrom, text_color="#ffffff", default_value=5, font=fonte14)],
        [sg.Text("CS", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="cs", background_color=marrom, text_color="#ffffff", default_value=5, font=fonte14)],
        [sg.Text("OD", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="od", background_color=marrom, text_color="#ffffff", default_value=5, font=fonte14)],
        [sg.Text("AR", background_color=roxo2, font=fonte16), sg.Combo(values= (valueDificulty), key="ar", background_color=marrom, text_color="#ffffff", default_value=5, font=fonte14)]
    ],
    layout = [
        [sg.Text(f"Seja bem vindo {name_user}\n",
            background_color="", font="Calibri 20 italic", text_color="#8253e6",
            enable_events=False)],
        [sg.TabGroup([

            [sg.Tab("Arquivo",configMapas, background_color=roxo1, key="Arquivo")],

            [sg.Tab("Metadata", configMetadata, background_color=roxo1, key="Metadata")],

            [sg.Tab("Dificuldade", configDificulty, background_color=roxo1, key="Dificuldade")],
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
    def apagarAnteriores():
                for file in os.listdir(valor_pasta):
                    if file.split(".")[1] == "osu":
                        os.remove(f"{valor_pasta}\{file}")
    apagarAnteriores()
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
            try:
                valorQuantidade = value["quantidadeDificuldades"]
                valorQuantidade = int(valorQuantidade)
                with open(r"uteis/Games/OSU/GeradorDeMapa/config.json", encoding="UTF-8", mode="r") as arquivo:
                    dados = json.load(arquivo)

                with open(r"uteis/Games/OSU/GeradorDeMapa/config.json",encoding="UTF-8", mode="w") as arquivo:
                    dados["Quantidade"] = valorQuantidade
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                    modfied(valorQuantidade)
                    window["METADATA"].update(values=dificults)
                    window["DIFICULDADE"].update(values=dificults)
            except ValueError:
                if valorQuantidade == "":
                    continue
                else:
                    [sg.popup("Por favor, digite apenas números inteiros")]

        elif event == "METADATA":
            dificuldadeMETADATA = value["METADATA"]
            print(dificuldadeMETADATA)

        elif event == "tittle":
            Titulo = value["tittle"]
            osu_blank_metadata["Title"] = Titulo
            #print(f"Titulo: {Titulo}")

        elif event == "unicodeTittle":
            TituloUnicode = value["unicodeTittle"]

            osu_blank_metadata["TitleUnicode"] = TituloUnicode

        elif event == "artist":
            Artista = value["artist"]
            osu_blank_metadata["Artist"] = Artista

        elif event == "unicodeArtist":
            ArtistaUnicode = value["unicodeArtist"]
            osu_blank_metadata["ArtistUnicode"] = ArtistaUnicode

        elif event == "creator":
            Criador = value["creator"]
            osu_blank_metadata["Creator"] = Criador

        elif event == "source":
            Fonte = value["source"]
            osu_blank_metadata["Source"] = Fonte

        elif event == "tags":
            Etiquetas = value["tags"]
            osu_blank_metadata["Tags"] = Etiquetas

        elif event == "countdown":
            Contagem = value["countdown"]
            if Contagem == True:
                print("Contagem ativada")
                Contagem = True
                osu_blank_genrl["CountDown"] = 1
            else:
                print("Contagem desativada")
                Contagem = False
                osu_blank_genrl["CountDown"] = 0

        elif event == "clickSound":
            if value["clickSound"] == False:
                with open(caminhoArquivo, mode="w", encoding="UTF-8") as arquivo:
                    dados["Audios"]["Click1"]["ativo"] = 0
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

            else:
                with open(caminhoArquivo, mode="w", encoding="UTF-8") as arquivo:
                    dados["Audios"]["Click1"]["ativo"] = 1
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

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
        elif event == "Gerar mapas":


            def aplicarMetadata():
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
                    [sg.popup("Preencha todos os campos de Metadata", background_color=roxo1, font=fonte12, button_color=(branco, cinza))]
                    window["Tab"].Widget.setCurrentIndex(1)
            aplicarMetadata()
            def gerarMapas():
                for dificult in dificults:
                    osu_blank_metadata["Version"] = dificult
                    osu_blank_genrl["AudioFilename"] = valor_audio.split("/")[-1]
                    texto = "osu file format v14\n\n[General]\n"

                    for nome, chave in osu_blank_genrl.items():
                        texto += (f"{nome}: {chave}\n")
                    texto += "\n[Editor]\n"
                    for nome, chave in osu_blank_editor.items():
                        texto += f"{nome}: {chave}\n"

                    texto += "\n[Metadata]\n"
                    for nome, chave in osu_blank_metadata.items():
                        texto+= f"{nome}: {chave}\n"
                    texto+= "\n[Difficulty]\n"
                    for nome, chave in osu_blank_dificculty.items():
                        texto += f"{nome}: {chave}\n"

                    texto += "\n[Events]\n"

                    for nome in osu_blank_events:
                        texto+= f"{nome}\n"

                    texto += "\n[HitObjects]\n"

                    with open(f"{valor_pasta}\[{dificult}].osu", mode="w", encoding="UTF-8") as arquivo:
                        arquivo.writelines(texto)
            gerarMapas()

        else:
            print(event)
    window.close()
Aplicativo()
