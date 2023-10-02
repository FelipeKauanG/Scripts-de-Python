import PySimpleGUI as sg
from random import sample



sg.theme("DarkBlue") # Tema


#Faz o layout do programa
layout = [[sg.Text("Sorteador da Mega Sena")], [sg.Button("Sortear"), sg.Button("Cancelar")]]

# Criar a janela
janela = sg.Window("Mega Sena", layout, size=(600, 200))

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
        break
    if evento == "Sortear":
        valores = []
        for i in range(1, 61):
            valores.append(i)
        sg.popup_ok(f"Valores sorteados {sample(valores, 6)}", text_color="#eeeeee", image=r"úteis\PysimpleGUI\title.png", title="MEGA SENA")
janela.close()
