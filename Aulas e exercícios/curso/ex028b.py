from random import randint
from time import sleep # importa a biblioteca time e peguei o sleep

computador = randint(0, 5)
print("Pensei no numero {}".format(computador)) #faz o computador sortear um numero
print("-=-"*10)
print("Vou pensesar em um numero entre 0 e 5. Tente adivinhar")
print("-=-"*10)
jogador = int(input("Em que numero eu pensei ?")) #jogador tenta adivinhar

print("Processando")

sleep(2)
if jogador == computador:
    print("Parabens, voce conseguiu me vencer")
else:
    print("GANHEI, eu pensei no numero {}, e nao no numero {}".format(computador, jogador))
