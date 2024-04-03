#Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo

print("Analise de numero primo: ")
num = int(input("Digite um numero: "))

for i in range(1, num):
    if num / (i % 0):
        print("Esse numero e primo")
    else:
        print("Esse numero nao e primo")
