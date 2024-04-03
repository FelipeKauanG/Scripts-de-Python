#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e taiz quadrada.abs

#Tente
try:
    #Seu código aqui
    def dobroTriploSqrt(num=0):
        """ 
        Este programa caslcula o dobro, o triplo e a raiz quadrada de um número.
        """

        print(f"\033[1m\nValor de {num}\033[m")
        print(f"\033[36mDobro de {num*2}\033[m")
        print(f"\033[34mTriplo de {num*3}\033[m")
        print(f"\033[33mRaiz quadrada de {num**0.5:.2f}\033[m")

    dobroTriploSqrt(85)

#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")