#Deselvolva um programa que leia seis numeros inteiros e mostre a soma apenas daquelas que forem pares.
# Se o valor digitado for impar, desconsidere - o

n1 = int(input("Valor um:"))
n2 = int(input("Valor dois:"))
n3 = int(input("Valor tres:"))
n4 = int(input("Valor quatro:"))
n5 = int(input("Valor cinco:"))
n6 = int(input("Valor seis:"))

if n1 % 2 == 1: n1 = 0
if n2 % 2 == 1: n2 = 0
if n3 % 2 == 1: n3 = 0
if n4 % 2 == 1: n4 = 0
if n5 % 2 == 1: n5 = 0
if n6 % 2 == 1: n6 = 0

print("A soma dos numeros pares sao \033[0;36m{}!\033[m".format(n1+n2+n3+n4+n5+n6))
