import PySimpleGUIQt as sg #pip install PySimpleGUIQ →
#pip install PySide6
import keyboard #pip install keyboard
import threading
from matplotlib import pyplot as plt

#Define o tema do PySimpleGUI
sg.theme("DarkPurple2")

#Lista a ser completada com valores
valores = []

#index atual 
index = 1
valAnterior = "Sem dados"

#Estrutura da janela
layout = [
    [sg.Text(f"Valor anterior {valAnterior}", key="ant", text_color="#ff7883", size=(40, 1))],
    [sg.Text(f"Valor {index}: ", key="index", text_color="#d6ff78"), sg.Input("", key="num")],
    [sg.Button("Continuar", size=(20, 1)), sg.Button("Terminar", size=(20, 1))],
    [sg.Cancel(size=(40, 1))]
     ]

#Declaraçã da janela e o título
window = sg.Window("Média aritmética", layout)


  

#Executção geral da janela
while True:
    try:

        #Declara os eventos e valores da janela do programa
        event, value = window.read()

        #Declara o valor de num sendo o valor da tupla "num"
        num = value["num"]

        #Formata o texto para o sistema padrão de números decimais
        num = str(num).replace(',', ".")
  
        #Faz uma tentativa se o valor é válido, caso não satisfaça, ele trata a exceção abaixo

        
        try:
            float(num) % 1
            
            #Se o usuário clicar em "continuar", ele adiciona o valor do input ao dicionário
            if event == "Continuar":

                #Número do index para informar ao usuário qual elemento ele está
                index += 1
                valores.append(float(num))
                valAnterior = num

                #Atualiza os valores no layout da janela
                window["index"].update(f"Valor {index}: ")
                window["ant"].update(f"Valor anterior ({str(valAnterior).replace('.', ",")}) ({len(valores)}º valor)")
                window["num"].update("")


        #Tratamento da exceção do valor inválido
        except:

            #Se o usuário fechar a janela
            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            #Se o usuário clicar em "Terminar
            elif event == "Terminar":
                window.close()

                # Calcula o valor da média
                media = sum(valores) / len(valores)

                mediaFormat = (f"{media:.2f}")


                #Função de mudar a cor do texto da média calculada
                def colorText(color):

                    #Função de criar um gráfico das notas
                    def mostrarGrafico():
                        plt.grid()
                        plt.style.use("fivethirtyeight")
                        plt.plot(valores)
                        plt.title(f'Média: {mediaFormat}')
                        plt.xlabel("Bimestres")
                        plt.ylabel("Notas")
                        plt.show()  

                    #Mostra o valor da média
                    [sg.popup(f"A média total foi {str(mediaFormat).replace('.', ",")}", text_color=f"{color}")]
                    mostrarGrafico()
                    
                
                #Se a média for entre 0 e 5
                if 0 <= media <= 5:
                    colorText(color="#f55142")
                    break

                #Se a média for maior 5 e menor que 7
                elif 5 < media < 7:
                    colorText(color="#f5c542")
                    break

                #se a média for maior ou igual a 7
                else:
                    colorText(color="#adf542")
                    break
                
            else:
                #Se caso o usuário nã digitar apenas números reais
                [sg.popup("Por favor, digite apenas números!")]


        


    #Se caso não tiver elementos suficientes
    except ZeroDivisionError:
        sg.popup("Programa encerrado com sucesso, pois não tenho elementos suficientes")
        window.close()
        break



#Fechar janelas
window.close()

print(f"\033[31mFim do programinha :)\033[m\n")
