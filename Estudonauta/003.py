import PySimpleGUI as sg

layout = [
    [sg.Text("Digite o primeiro número"), sg.Input("", key="num1")],
    [sg.Text("Digite o segundo número"), sg.Input("", key="num2")],
    [sg.Button('OK'), sg.Button('Cancelar')]
]

window = sg.Window("Soma entre dois números", layout)

while True:
    event, value = window.read()
    num1 = value["num1"]
    num2 = value["num2"]

    if event == "Cancelar" or event == sg.WIN_CLOSED:
        break

    if event == "OK":
        print(f"\nA soma entre \033[31m{num1}\033[m e \033[34m{num2}\033[m = \033[35m{int(num1) + int(num2)}\033[m")
        break

print(f'\n\033[31mFim do programinha\033[m')
