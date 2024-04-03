#Faca um programa que leia tres numeros e mostre na tela qual e o maior e qual e o menor

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro Valor: "))
#verificando quem e o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# quem e o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior valor digitado foi \033[0;34m{}\033[m".format(maior))
print("O menor valor digitado foi \033[0;31m{}\033[m".format(menor))

