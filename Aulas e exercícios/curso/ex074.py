#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
#Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que
#estao na tupla.

from random import randint

numeros = randint(0, 10), randint(0, 10),\
    randint(0, 10), randint(0, 10), randint(0, 10)

print(f"""\033[0;32m{numeros}\033[m""", end="")

#print(f"\nO maior valor e \033[0;36m{organi[4]}\033[m")
#print(f"O menor valor e \033[0;34m{organi[0]}\033[m")
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")