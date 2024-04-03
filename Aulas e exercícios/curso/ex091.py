# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario.
# No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero do dado.

from random import randint
from time import sleep

dados = {}
ordem = list()
for i in range(1, 5):
    dados[f"Jogador {i}"] = str(randint(1, 6))

for j, i in dados.items():
    print(f"O {j} tirou \033[0;34m{i}\033[m")
    sleep(0.5)
print("\033[0;36;4m▄\033[m" * 40)
print()
print("\033[0;96mRanking de maiores numeros\033[m")

for k, v in dados.items():
    ordem.append(v + k)

ordem.sort()

for l in range(3, -1, -1):
    print(f"Lugar\033[0;95m{ordem[l][1:]}\033[m Com \033[0;35m{ordem[l][0]}\033[m")
    sleep(0.5)
