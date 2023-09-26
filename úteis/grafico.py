import PySimpleGUI as sg

sg.theme("DarkAmber")
layout = [
    [sg.Text("Nome"), sg.Input(""), sg.Button("Corrigir")],
    [sg.Text("Senha"), sg.Input("")],
    [sg.Button("Cadastrar")]
]
window = sg.Window("Aplicativo", layout)
event, value = window.read()
