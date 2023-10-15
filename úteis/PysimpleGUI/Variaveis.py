import PySimpleGUI as sg

# Defina o layout da tela
layout = [
    [sg.Text("Digite seu nome")],
    [sg.InputText(key="nome")],
    [sg.Button("ok"), sg.Button("Sair")]
]

# Crie uma janela
window = sg.Window("Inserir nome", layout)

# Loop de evento
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    if event == "ok":
        nome = values['nome']
        sg.popup(f"Seu nome é : {nome}")

# Feche a janela
window.close()
