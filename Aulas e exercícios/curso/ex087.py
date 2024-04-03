#Aprimore o desafio anterior, mostrando no final:

#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []
soma = 0
for i in range(0, 9):
    n = int(input("Valor: "))
    matriz.append(n)
print(f"""\033[0;32m[{matriz[0]}]  [{matriz[1]}]  [{matriz[2]}]
[{matriz[3]}]  [{matriz[4]}]  [{matriz[5]}]
[{matriz[6]}]  [{matriz[7]}]  [{matriz[8]}]\033[m""")

for pares in matriz:
    if pares % 2 == 0:
        soma += pares
print(f"A soma dos numeros \033[4mpares\033[m e igual a  \033[0;36m{soma}\033[m")
print(f"""A soma da \033[4mterceira\033[m coluna e igual a \033[0;34m{matriz[2]+matriz[5]+matriz[8]}\033[m""")
print(f"""A soma da \033[4msegunda\033[m linha e igual a \033[0;31m{matriz[3]+matriz[4]+matriz[5]}\033[m""")
