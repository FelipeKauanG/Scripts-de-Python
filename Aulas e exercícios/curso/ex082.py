#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteudo das tres listas geradas.
from time import sleep
pares = []
impares = []

while True:
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    per = str(input("Quer continuar ?")).lower().strip()
    if per not in "sn":
        per = str(input("Quer continuar ?")).lower().strip()
    if per == "n":
        break

for i in range(0, 20):
    sleep(0.02)
    print("\033[0;31m•\033[m", end="")

for i in range(0, 20):
    sleep(0.02)
    print("\033[0;32m•\033[m", end="")

for i in range(0, 20):
    sleep(0.02)
    print("\033[0;34m•\033[m", end="")


print(f"\nA lista completa e \033[0;35m{sorted(pares+impares)}\033[m")
print(f"Pares sao \033[0;34m{sorted(pares)}\033[m")
print(f"Impares sao \033[0;31m{sorted(impares)}\033[m")
