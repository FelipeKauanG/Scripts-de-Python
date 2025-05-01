import PySimpleGUIQt as sg

# Layouts para cada aba
layout_arquivo = [
    [sg.Text("Selecione uma pasta:")],
    [sg.FolderBrowse("Procurar pasta", key="pasta", enable_events=True)],
    [sg.Text("", size=(40, 1), key="caminhoPasta")],
]

layout_metadata = [
    [sg.Text("Digite o título:")],
    [sg.Input(key="titulo")],
]

layout_dificuldade = [
    [sg.Text("Escolha a dificuldade:")],
    [sg.Combo(["Easy", "Normal", "Hard"], key="dificuldade")],
]

# TabGroup com abas
layout = [
    [sg.TabGroup(
        [[
            sg.Tab("Arquivo", layout_arquivo, key="Arquivo"),
            sg.Tab("Metadata", layout_metadata, key="Metadata"),
            sg.Tab("Dificuldade", layout_dificuldade, key="Dificuldade"),
        ]],
        key="TabGroup",
        enable_events=True  # Habilita eventos ao trocar de aba
    )],
    [sg.Button("Fechar")]
]

# Criação da janela
window = sg.Window("Exemplo de TabGroup", layout, finalize=True)

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Fechar":
        break

    # Evento ao trocar de aba
    if event == "TabGroup":
        aba_atual = values["TabGroup"]  # Aba ativa
        print(f"Aba ativa: {aba_atual}")

        # Validação antes de permitir troca de aba
        if aba_atual == "Metadata":
            if values["pasta"] == "":
                sg.popup("Por favor, selecione uma pasta antes de avançar!")
                window["TabGroup"].update(selected_title="Arquivo")  # Volta para a aba "Arquivo"
        elif aba_atual == "Dificuldade":
            if values["titulo"] == "":
                sg.popup("Por favor, preencha o título antes de avançar!")
                window["TabGroup"].update(selected_title="Metadata")  # Volta para a aba "Metadata"

window.close()