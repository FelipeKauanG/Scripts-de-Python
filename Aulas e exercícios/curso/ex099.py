#Faca um programa que tenha um funcao maior que receba varios parametros com valores inteiros.
#Sei programa tem que analisar todos os valores e dizer qual deles e o maior.
from time import sleep
def maior(*num):
    if len(num) == 0:
        print("=" * 30)
        print(f"Voce nao informou nenhum valor!")
        print("=" * 30)
    else:
        print("="*30)
        print("Analizando os valores passados...")
        print(f"\033[0;34m{num}\033[m Foram informados \033[0;36m{len(num)}\033[m ao todo")
        print(f"O maior valor informado foi {max(num)}")
        print("="*30)
        print()
        sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
