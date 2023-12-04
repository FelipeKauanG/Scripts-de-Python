import PySimpleGUI as sg
from PIL import Image

layout = [
    [sg.Text("Selecione uma imagem em formato PNG:", justification="Center")],
    [sg.InputText(key="image_path"), sg.FileBrowse(file_types=(("Imagens PNG", "*.png"), ("Imagens JPG", "*.jpg")))],
    [sg.Button("Abrir Imagem"), sg.Button("Sair"), sg.Checkbox("Mostrar gráfico", default=False, key="toggle_button")]
]

window = sg.Window("Abrir imagem", layout, element_justification='c', finalize=True)

while True:
    event, values = window.Read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "Abrir Imagem":
        imagem_path = values["image_path"]
        if imagem_path:
            img = Image.open(imagem_path)
            img.show()

window.close()
