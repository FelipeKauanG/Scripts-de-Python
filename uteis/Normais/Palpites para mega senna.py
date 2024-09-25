#Faca um programa que ajude um jogador da mega sena a criar palpites. O programa
#vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.

from random import sample
from time import sleep

print("Sorteador da Mega Sena")

val = int(input("Quantos jogos quer que eu sorteio ?"))
valores = []
for i in range(1, 61):
    valores.append(i)
for v in range(1, val+1):
    print(f"Jogo {v} \033[0;36m{sorted(sample(valores, k=6))}\033[m")
    sleep(0.1)
