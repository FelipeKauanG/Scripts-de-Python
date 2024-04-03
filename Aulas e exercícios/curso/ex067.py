#faca um programa que mostre a tabuada de varios numeros, um valor digitado pelo
# usuario. O programa sera interrompido quando o numero solicitado for negativo.

from time import sleep
num = 1
while num > -1:
    num = int(input("Quer ver a tabuada de qual valor ?"))
    tab = 0
    if num < 0:
        break
    while tab != 10:
        tab += 1
        print(f"{num} x {tab} = {num*tab}")
print("Finalizando a tabuada")
for i in range (0, 3):
    sleep(0.5)
    print(".", end="")
