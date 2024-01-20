import os
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from time import sleep


pasta = os.listdir(r"PixelArtMinecraft\blocos")
cores = []
novaImagem = Image.open(r"PixelArtMinecraft\imagem\PixelArt.png")
largura, altura = novaImagem.size
novaImagem.convert("RGBA")
totalPixels = novaImagem.size[0] * novaImagem.size[1]

for x in range(0, altura):
    for y in range(0, largura):
        cor = novaImagem.getpixel((y, x))
        r = int(cor[0])
        g = int(cor[1])
        b = int(cor[2])
        hexColor = r, g, b
        cores.append(hexColor)
paleta = []
for bloco in pasta:
    imagem = Image.open(f"PixelArtMinecraft/blocos/{bloco}")
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
    for pal in paleta:
        melhorBloco = []
        corR = int(cor[0])
        corG = int(cor[1])
        corB = int(cor[2])
        media = True
        palR = int(str(pal).split(";")[1].split(",")[
                   0].replace("(", "").replace(")", ""))
        palG = int(str(pal).split(";")[1].split(",")[
                   1].replace("(", "").replace(")", ""))
        palB = int(str(pal).split(";")[1].split(",")[
                   2].replace("(", "").replace(")", ""))

        correspondencia = True

        print(f"\033[31m{palR, palG, palB} - {str(pal).split(";")[0]}\033[m")
        print(f"\033[34m{corR, corG, corB} \033[m")
        sleep(1)


def mostrarFoto():
    cores = np.array(cores).reshape(altura, largura, 3)
    plt.imshow(cores)
    plt.axis("off")
    plt.show()
