# Crie um programa que gerencia o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o
# campeonato.

dados = {}

dados["jogador"] = str(input("Nome do jogador: "))
dados["partidas"] = int(input("Partidas: "))
gols = list()
total = 0
for k in range(dados['partidas']):
    gol = int(input(f"Quantos gols {dados['jogador'].strip().title()} na \033[0;94m{k+1}a\033[m partida"))
    total += gol
    gols.append(gol)
dados["Gol"] = gols.copy()
print()
for g in range(dados["partidas"]):
    print(f"   → Na \033[0;32m{g+1}a\033[m partida, {dados['jogador'].title().strip()} fez \033[0;33m{gols[g]}\033[m gol(s)")

print(f"\nSaldo de \033[0;32m{total}\033[m gol(s)")
print("FIM")
