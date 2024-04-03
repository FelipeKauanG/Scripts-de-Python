#Escreva um programa que leia um número Inteiro e mostr na tela seu sucessor e seu antecessor.

#Tente
try:
    #Seu código aqui
    def sucessorAntecessor(num):
        """
        Este programa verifica o seu sucessor e seu antecessor.
        """
        print(f"\033[31mAntecessor: {num-1}\033[m")
        print(f"\033[32mNúmero: {num}\033[m")
        print(f"\033[34mSucessor: {num+1}\033[m")
 
    sucessorAntecessor(3)
    


#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")