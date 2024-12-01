import PySimpleGUIQt as sg

sg.theme("DarkPurple2")

#Primeiro Layout
layout = [
    [sg.Text("Digite um número e vamos calcular o seu dobro, triplo e raíz quadrada")],
    [sg.Input(key="num", enable_events=True)],
    [sg.OK(), sg.Cancel()]
]

window = sg.Window("Dobro, tiplo e raíz quadrada", layout)


#Executando a primeira janela
while True:
    event, value = window.read()
    num = value["num"]

    #Se o evento for o botão cancelar ou fechar, encerra a janela
    if value == "Cancel" or value == sg.WIN_CLOSED:
        break
    
    elif event == "OK":
        #Criando outro layout para os resultados
        res = [
            [sg.Text(f"Número: {num}")],
            [sg.Text(f"Dobro {int(num)*2}"),
            sg.Text(f"Triplo: {int(num)*3}"),
            sg.Text(f"Raíz quadrada: {float(num)**0.5}")],
            [sg.Button("Terminar")]
        ]
        window.close()
        layout = None
        break

#Carregar a nova janela dos resultados
layout = sg.Window("Resultados", res)


#Executar a nova janela dos resultados
while True:
    event, value = layout.read()

    if event == sg.WIN_CLOSED or event == "Terminar":
        break

window.close()

print(f"\n\033[31mFim do programinha :)\033[m\n")
