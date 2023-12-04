import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import fractions

sg.theme("DarkAmber")

layout = [[sg.Image("")][sg.FileBrowse("Procurar imagem")], [sg.Button("Cancel")]]

window = sg.Window("Pixel Mosaic Minecraft", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    window.close()