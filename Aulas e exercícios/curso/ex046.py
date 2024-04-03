#Faca um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio
#indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
from time import sleep

for i in range(10, -1, -1):
    print("\033[0;36m{}\033[m".format(i))
    sleep(1)
