# faca um programa que tenha um funcao chamada ficha que tenha dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou.
#O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado
# corretamente.

def ficha(jog="Desconhecido", gol="0"):
    if jog.isalpha():
        print(f"O jogador {jog.title()}",end=" ")
    else:
        print(f"O jogador <desconhecido> ", end="")
    if gol.isnumeric():
        print(f"marcou {gol} gol(s) no campeonato")
    else:
        print("marcou 0 gols no campeonato")


ficha(str(input("Nome do jogador: ")), str(input("Quantidade de gols: ")))
