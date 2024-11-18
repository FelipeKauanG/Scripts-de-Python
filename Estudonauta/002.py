import PySimpleGUI as sg
nome = ""
layout = [
    [sg.Text("Digite o seu nome")],
    [sg.Input("")], 
    [sg.Button("OK"), sg.Button("Cancelar", key="nome")],
]


sg.theme("Dark2")

window = sg.Window("Respondendo ao usuário", layout)

print()
while True:
    event, value = window.read()

    if event == "OK":
        print(f"Seja bem vindo(a) \033[33m{str(value[0]).capitalize()}\033[m")
        break
    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break

print(f"\n\033[31mFim do programa\033[m")
