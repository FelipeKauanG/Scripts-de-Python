import PySimpleGUIQt as sg

# Layout das abas
tab1_layout = [[sg.Text("Conteúdo da Aba 1")]]
tab2_layout = [[sg.Text("Conteúdo da Aba 2")]]
tab3_layout = [[sg.Text("Conteúdo da Aba 3")]]

# Layout principal com o TabGroup
layout = [
    [sg.TabGroup(
        [[sg.Tab("Aba 1", tab1_layout, key="Tab1"),
          sg.Tab("Aba 2", tab2_layout, key="Tab2"),
          sg.Tab("Aba 3", tab3_layout, key="Tab3")]],
        key="TabGroup",
        enable_events=True
    )],
    [sg.Button("Ir para Aba 2", key="GoToTab2"), sg.Button("Ir para Aba 3", key="GoToTab3")],
    [sg.Button("Sair")]
]

# Criação da janela
window = sg.Window("Exemplo de Navegação entre Abas", layout)

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break

    # Alternar para a Aba 2
    if event == "GoToTab2":
        window["TabGroup"].Widget.setCurrentIndex(1)  # Índice da Aba 2 (começa em 0)

    # Alternar para a Aba 3
    elif event == "GoToTab3":
        window["TabGroup"].Widget.setCurrentIndex(2)  # Índice da Aba 3 (começa em 0)

# Fechar a janela
window.close()