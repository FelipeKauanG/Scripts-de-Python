#Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada.

#Tente
try:
    #Seu código aqui
    """
        Ester programa calcula a tabuada de um valor inteiro qualquer.
    """
    print()
    def linhas():
        print(f"\033[35m=-\033[m"*18)
    def tabuada(num=0):
        linhas()
        print(f"\t\033[35;7mTabuada do {num}\033[m")
        for row in range(1, 11):
            print(f"\t\033[36;1m {num} * {row} =\033[m \033[32m{row*num}\033[m")
            
        linhas()
    
    tabuada(11)
#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")


except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")