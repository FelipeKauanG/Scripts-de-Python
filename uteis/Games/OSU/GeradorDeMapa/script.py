import PySimpleGUIQt as sg
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

print(dados)

# tema da janela
sg.theme("Dark")
quantidades = 6

# ===========================================================================
#
#                           CONFIGURAÇÃO DOS MAPAS
#
# =========================================================================



def configuracaoMapa():
    # Dificuldades padrões
    dificults = ["Easy", "Normal", "Hard", "Insane", "Expert", "Expert+"]


    if quantidades > len(dificults):
        for i in range(quantidades - (len(dificults))):
            dificults.append("~em branco~")
    else:
        for i in range(len(dificults) - quantidades):
            dificults.pop(-1)


    #Layout das configurações
    layoutConfig = [
        [sg.Text("Dificuldade: ")],
        [sg.Combo(dificults, key="dificuldade")],
        [sg.Input("", key="nomeDificuldade")],
        [sg.Button("Renomear dificuldade", key="renomear")],
        [sg.Ok(), sg.Cancel("Cancelar")],
    ]

    window = sg.Window("Configuração dos mapas", layoutConfig)

# Janela para a configuração dos mapas
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        
        # Se evento for renomear
        if event == "renomear":

            # Caso não tiver nada escrito
            if values["nomeDificuldade"] == "":
                [sg.popup("Por favor, insira o nome da dificuldade!")]

            # Execução de renomear
            else:
                index = dificults.index(values["dificuldade"])
                nome = values["nomeDificuldade"]

                dificults[index] = nome

                window["dificuldade"].update(values=dificults)
                window["nomeDificuldade"].update("")

        if event == "Ok":
            quantBranco = 0
            for dificuldade in dificults:
                if dificuldade == "~em branco~":
                    quantBranco += 1

            if quantBranco == 1:
                sg.popup(f"Tem apenas uma dificuldade em branco")
            elif quantBranco > 1:
                sg.popup(f"Existem {quantBranco} dificuldades em branco")
            else:
                print(dificults)
                break
    window.close()



# ===========================================================================
#
#                                   METADADOS
#
# ===========================================================================


def metadados():
    # Seleção de pasta
    layoutPasta = [
        [sg.Text(valor_pasta, visible=True, key="caminhoPasta", justification="center")],
        [sg.FolderBrowse("Procurar pasta", key="pasta", initial_folder=desktop_path)], [sg.Button("Atualizar caminho da pasta", key="atualizarPasta")]
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
        [sg.Text("Quantidade de mapas"), sg.Input(key="quantidadeDificuldades", default_text=quantidades)],
        [sg.Frame("Seleção de audio", layoutAudio)],
        [sg.Frame("Formulário", formulario)],
        [sg.Ok(), sg.Cancel("Cancelar")]
        ]
    reposta = "no"

    window = sg.Window("metadados", layout)

    #Carregar a janela dos metadados
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar":
            break
        if event == "atualizarPasta":
            if values["pasta"] == None:
                [sg.popup("Por favor, digite um nome para a pasta!")]
                
            else:
                # Reescreve o caminho da pasta
                with open(caminho_arquivo, encoding="UTF-8", mode="w") as arquivo:
                    dados["mapas_path"] = values["pasta"]
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                    print(values)
                window["caminhoPasta"].update(values["pasta"], visible=True)


        if event == "atualizarAudio":
            window["caminhoAudio"].update(values["audio"], visible=True)
        if event == "Ok":
            print()
            for nome in values:
                if not values["pasta"]:
                    [sg.popup("Selecione uma pasta")]
                    break
                
                if not values["quantidadeDificuldades"]:
                    [sg.popup("Preencha o campo de quantidade de mapa")]
                    break

                elif values["quantidadeDificuldades"].isnumeric() == False:
                    [sg.popup("Por favor, digite apenas números!")]
                    break

                elif int(values["quantidadeDificuldades"]) < 1:
                    [sg.popup("Por favor, digite apenas números positivos\nno campo de quantidade de dificuldades!")]
                    break
                
                # Se a quantidade de dificuldades for maior que 10
                elif int(values["quantidadeDificuldades"]) > 10 and reposta == "no":

                    evento = sg.popup_yes_no("Você tem certeza que deseja criar mais de 10 dificuldades?")

                    if evento == "Yes":
                        reposta = "yes"
                        pass
                    else:
                        values["quantidadeDificuldades"] = ""
                        break
                    break
                

                #Se não tiver cada uma das lacunas abaixo
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
                    print(values)

                break

    window.close()

metadados()
