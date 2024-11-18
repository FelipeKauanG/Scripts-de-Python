import PySimpleGUI as sg

layout = [
    [sg.Input(),sg.FileBrowse("Procurar um arquivo")],
    [sg.Ok("OK", key="ok"), sg.Text("Cancelar")]
]

sg.theme("Dark")

window = sg.Window("Aplicativo", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break

window.close()
