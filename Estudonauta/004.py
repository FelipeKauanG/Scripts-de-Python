import PySimpleGUI as sg


valor = 1


def tipo(valor):
    
    if type(valor) == type(1):
        res = "Inteiro"
        return res
    
    elif type(valor) == type(1.1):
        res = "Decimal"
        return res
    
    elif type(valor) == type("String"):
        res = "String"
        return res
    
    elif type(valor) == type(True):
        res = "Booleano"
        return res


layout = [
    [sg.Text(f'O tipo primitivo de {valor} é {tipo(valor)}')],
    [sg.Button("OK")]
]


window = sg.Window("Tipo primitivo", layout)


while True:
    event, value = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

print(f'\n\033[31mFim do programinha\033[m')
