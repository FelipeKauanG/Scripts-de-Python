#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros

#Tente
try:
    #Seu código aqui
    def conversorDeMedidas(metros=0):
        """
            Este programa converte o valor em metros para centímetros e milímetros
        """
        print(f"\033[1m\nValor em metros: {metros}\033[m")
        print(f"\033[32mValor em centimetros: {metros*100} cm\033[m")
        print(f"\033[33mValor em milímetros: {metros*1000} mm\033[m")

    conversorDeMedidas(3)

#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")
     