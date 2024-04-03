#Faca um programa que leia um ano qualquer e mostre na tela se ele e bissexto

ano = int(input("Ano: "))

if ano % 4 == 0:

    print("e um ano \033[0;32mbissexto\033[m")
else:
    print("Ano \033[0;33mnormal\033[m")
