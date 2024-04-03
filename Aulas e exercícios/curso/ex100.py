#Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio() e somaPar().
#A primeira funcao vai sortear 5 numeros e vai coloca -
#los dentro da lista e a segunda funcao vai mostrar a
#soma entre todos os valores pares sorteados pela funcao anterior.
from random import randint
num = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), ]
def sorteio():
    print(f"Sorteando 5 valores {num}".replace("[", "").replace("]", ""))


def somapar():
    soma = 0
    for nume in num:
        if nume % 2 == 0:
            soma += nume

    print(f"A soma dos valores pares sao \033[0;36m{soma}\033[m")


sorteio()
somapar()
