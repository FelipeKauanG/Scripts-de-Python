import PySimpleGUI as sg #pip install PySimpleGUIQ
import numpy as np #pip install numpy
from matplotlib import pyplot as plt # pip install matplotlib
from time import sleep
import os
from tkinter import *
from fractions import Fraction
from PIL import Image


pasta = os.listdir(r"PixelArtMinecraft\blocos")
for bloco in pasta:
    imagem = Image.open(f"PixelArtMinecraft/blocos/{bloco}")
    imagem = imagem.convert("RGB")
    largura,altura = imagem.size
    #print(f"Largura: {largura}x{altura}")
    print(f"\033[32m{bloco}\033[m")
    
    



print(len(pasta))
