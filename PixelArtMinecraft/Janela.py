import PySimpleGUI as sg


layout = [

    [sg.Text("Algum texto em coluna")], 
    [sg.Text("'Enter' alguma coisa em linha 2"), sg.InputText()],
    [sg.Button("OK"), sg.Button("Cancel")]
    ]


window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    print("You entered ", values[0])

window.Close()
