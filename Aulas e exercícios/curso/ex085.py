#Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre em
# uma lista unica e que mantenha separados os valores pares e impares. No final,
# mostre os valores pares e impares em ordem crescente.

valores = [[], []]
for i in range(1, 8):
    n = int(input(f"Digite o {i}o valor: "))
    if n % 2 == 0:
        valores[0].append(n)
    elif n % 2 == 1:
        valores[1].append(n)
print(f"""Valores pares \033[0;36m{sorted(valores[0])}\033[m
Valores impares \033[0;31m{sorted(valores[1])}\033[m""")
