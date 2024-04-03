#Faca um programa que leia um numero qualquer e mostre o seu fatorial.
#ex 5! = 5x4x3x2x1 = 120

print("Calculadora de fatorial:")
n = int(input("Valor do fatorial:  "))
n1 = 1
for i in range(n, 1, -1):
    print(i, end=" x ")
    n1 *= i
print("\033[0;32m = \n{}\033[m".format(n1))
