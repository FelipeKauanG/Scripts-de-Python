import PySimpleGUI as sg

sg.theme('Dark')
layout = [
    [sg.Text("Digite um númerio inteiro"), sg.InputText("", key="num1")],
    [sg.Button("OK"), sg.Button("Cancelar")]
]


window = sg.Window("Programa", layout)


while True:
    event, value = window.read()
    num1 = value["num1"]
    num1 = int(num1)

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break
    else:
        [sg.Popup(f"Antecessor: {num1-1}",text_color="#ff7575")],
        [sg.Popup(f"Número: {num1}",text_color="#fff280")],
        [sg.Popup(f"Sucessor: {num1+1}",text_color="#b1ff80")],
