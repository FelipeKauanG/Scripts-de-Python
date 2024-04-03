#Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
#no final mostre a matriz na tela, com a formatacao corrreta.

matriz = []

for i in range(0, 9):
    matriz.append(int(input("Valor da matriz: ")))
print("-="*15)


print(f"""\033[0;33m        [{matriz[0]}]  [{matriz[1]}]  [{matriz[2]}]
        [{matriz[3]}]  [{matriz[4]}]  [{matriz[5]}]
        [{matriz[6]}]  [{matriz[7]}]  [{matriz[8]}]\033[m""")
print("-="*15)
