import PySimpleGUI as sg
import time

def mostrar_barra_progresso():
    layout = [[sg.Text("Processando:")],
              [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Button("Iniciar"), sg.Button("Cancelar")]]

    window = sg.Window("Barra de Progresso", layout)

    while True:
        event, values = window.read(timeout=100)  # tempo de atualização em milissegundos

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break

        if event == "Iniciar":
            for i in range(100):
                window['progressbar'].update_bar(i + 0.5)
                time.sleep(0.2)  # Simulação de uma operação demorada

    window.close()

mostrar_barra_progresso()
