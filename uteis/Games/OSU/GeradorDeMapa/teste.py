import PySimpleGUIQt as sg

# Layout da interface
layout = [
    [sg.Text("Selecione um arquivo:")],
    [sg.Input(key="-FILE-"), sg.FilesBrowse(file_types=(("Arquivos de Texto", "*.txt"), ("Imagens PNG", "*.png"), ("Todos os Arquivos", "*.*")))],
    [sg.Button("Confirmar"), sg.Button("Cancelar")]
]

# Criação da janela
window = sg.Window("Selecionar Arquivo", layout)

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancelar":
        break
    elif event == "Confirmar":
        arquivo_selecionado = values["-FILE-"]
        sg.popup(f"Arquivo(s) selecionado(s): {arquivo_selecionado}")

# Fechamento da janela
window.close()
