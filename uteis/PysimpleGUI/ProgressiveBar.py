import PySimpleGUI as sg

layout = [
    [sg.ProgressBar(max_value=100, orientation="h", bar_color=(0xff00ff, 0xffffff), size=(60, 20), key="progressBar")],
    [sg.Button("OK"),sg.Button("Cancel")]
]

window = sg.Window("Progress Bar", layout)



num = 1
while True:
    events, values = window.read()

    if events == "Cancel" or events == sg.WIN_CLOSED:
        break

    elif events == "OK":
        window["progressBar"].update(num)
        num += 1
    if num == 100:
        break