import PySimpleGUI as sg

layout = [
    [sg.Text("Olá, mundo")],
    [sg.Button("Fechar")]
]

window = sg.Window("Aula 001", layout)

while True:
    event, values = window.read()

    if event == "Fechar" or event == sg.WIN_CLOSED:
        break

print('Fim do programa')
