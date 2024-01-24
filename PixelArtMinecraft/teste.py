import os
from PIL import Image
import numpy as np
from PIL import Image
from time import sleep
from matplotlib import pyplot as plt


pasta = os.listdir(r"PixelArtMinecraft\blocos")
transparente = []
for bloco in pasta:
    imagem = Image.open(f"PixelArtMinecraft/blocos/{bloco}")
    imagem = imagem.convert("RGBA")
    for x in range(0, 16):
        for y in range(0, 16):
            cor = imagem.getpixel((x, y))
    if cor[3] != 255 and bloco not in "glass":
        transparente.append(bloco)
        
    #sleep(100)
print(transparente)