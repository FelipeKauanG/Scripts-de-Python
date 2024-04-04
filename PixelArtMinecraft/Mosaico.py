import os
from PIL import Image #pip install Pillow
import numpy as np #pip install numpy
from matplotlib import pyplot as plt #pip install matplotlib
import PySimpleGUI as sg #pip install PySimpleGUI



sg.theme("Darkblue")
choiceIMG = [
    [sg.FileBrowse("Procurar arquivo")],
    [sg.Button("OK"), sg.Button("Cancelar")],
    [sg.Check("Mostrar Imagem"), sg.Check("Salvar Imagem")],
    [sg.ProgressBar(100, orientation="h", size=(20, 20), key="progressBar")]
]

choice = sg.Window("Escolher imagem", choiceIMG)

while True:
    event, values = choice.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    novaImagem = Image.open(values["Procurar arquivo"])
    nomeImagem = str(values["Procurar arquivo"]).split("/")[-1]
    mostra = values[0]
    salvar = values[1]
    break
choice.close()


del(values, choice, choiceIMG, event)
try:
    pasta = os.listdir(r"PixelArtMinecraft/blocos")
except FileNotFoundError:
    pasta = os.listdir(r"blocos")

cores = []
novaImagem = novaImagem.convert("RGBA")
largura, altura = novaImagem.size
print(largura, altura)

totalPixels = novaImagem.size[0] * novaImagem.size[1]

for x in range(0, altura):
    for y in range(0, largura):
        cor = novaImagem.getpixel((y, x))
        r = cor[0]
        g = cor[1]
        b = cor[2]
        hexColor = r, g, b
        cores.append(hexColor)
paleta = []
for bloco in pasta:
    try:
        imagem = Image.open(f"PixelArtMinecraft/blocos/{bloco}")
    except FileNotFoundError:
        imagem = Image.open(f"blocos/{bloco}")

    imagem = imagem.convert("RGBA")
    LARGURA, ALTURA = imagem.size
    R = 0
    G = 0
    B = 0

    for X in range(0, LARGURA):

        Y = 0
        Y += 1
        R += imagem.getpixel((X, Y))[0]//16
        G += imagem.getpixel((X, Y))[1]//16
        B += imagem.getpixel((X, Y))[2]//16
        conjunto = (f"{bloco};{R, G, B}")
        if Y > ALTURA:
            Y = 0

        paleta.append(conjunto)

grafico = []
for cor in cores:
    melhorBloco = []
    for pal in paleta:
        corR = int(cor[0])
        corG = int(cor[1])
        corB = int(cor[2])
        palR = int(str(pal).split(";")[1].split(",")[0].replace("(", "").replace(")", ""))
        palG = int(str(pal).split(";")[1].split(",")[1].replace("(", "").replace(")", ""))
        palB = int(str(pal).split(";")[1].split(",")[2].replace("(", "").replace(")", ""))
        mediaR = abs((corR - palR))
        mediaG = abs((corG - palG))
        mediaB = abs((corB - palB))
        mediaGeral = (mediaR + mediaG + mediaB) // 3
        correspondencia = (f"{mediaGeral} {str(pal).split(";")[0]}")
        melhorBloco.append(correspondencia)
        # print(f"{mediaR}%, {mediaG}%, {mediaB}%")
    # sleep(1000)

    def extrairCor(cor):
        return float(cor.split()[0])

    melhorBloco = sorted(melhorBloco, key=extrairCor)
    grafico.append(f"{str(melhorBloco[0]).split(" ")[1]}")
    # print(grafico)
    # sleep(1000)
foto = []
imagemBranco = Image.new("RGBA", (largura*16, altura*16), color="white")
x = 0
y = 0

for bloco in grafico:
    try:
        ImagemBloco = Image.open(os.path.join(r"PixelArtMinecraft/blocos", bloco))
    except FileNotFoundError:
        ImagemBloco = Image.open(os.path.join(r"blocos", bloco))
    

    imagemBranco.paste(ImagemBloco, (x, y))
    x += 16
    if x >= largura*16:
        x = 0
        y += 16
cores = np.array(cores).reshape(largura, altura, 3)

def mostrarGrafico():
    plt.show()
    plt.imshow(cores)


def mostrarImagem():
    if mostra == True:
        imagemBranco.show()
    if salvar == True:
        saveIMG = [
            [sg.FolderBrowse("Salvar Imagem")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        save = sg.Window("Salvar Imagem", saveIMG)
        while True:
            event, values = save.read()
            if event == sg.WIN_CLOSED or event == "Cancelar":
                break
            imagemBranco.save(f"{values['Salvar Imagem']}/{nomeImagem}")
            
            break
        save.close()


mostrarImagem()

