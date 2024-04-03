#melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero entre 0 a 10.
#so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint

print("\033[0;34mOla!! eu sou o computador, tente adivinhar um numero que pensei!!!\033[m")


print("\n\033[4mDica: Voce tem numeros de 0 a 10 para acertar.\033[m")


comp = randint(0, 10)
jogadas = 0
r = 11

while r != comp:
    r = int(input("Valor: "))
    jogadas += 1
if jogadas == 1:
    print("\033[0;33mDe primeira em\033[m")
print("Foi um total de \033[0;34m{}\033[m jogadas".format(jogadas))
print("Eu pensei em \033[0;35m{}\033[m \033[0;31mPARABENS\033[m".format(comp))
