# Aprimore o desadio 093 para que ele funcione com varios jogadores,
# incluindo um sistema de visualizacao de detalhes do aproveitamento de cada jogador.
from time import sleep
print("Cadastro do jogadores e aproveitamento")
dados = dict()
lista = list()
gols = list()
while True:
    gols.clear()
    dados["Nome"] = str(input("\nNome do jogador: ")).strip().title()
    total = int(input(f"Quantas partidas \033[0;95m{dados['Nome']}\033[m jogou ?"))
    for partidas in range(0, total):
        gols.append(int(input(f"Quantas gols {dados['Nome']} fez na {partidas+1}a partida ?")))
        dados["Gols"] = gols.copy()
        dados["Saldo"] = sum(dados["Gols"])
    lista.append(dados.copy())

    per = str(input("Quer continuar ? [S/N]")).lower().strip()[0]
    while per not in "sn":
        per = str(input("Digite [S/N]"))
    if per == "n":
        break

print("=-="*30)
print()
print()
print("No  Nome:                                          Saldo:")

for g in range(0, len(lista)):
    print(f"{g+1}  \033[0;95m{lista[g]['Nome']}\033[m", " "*(45-(len(lista[g]['Nome']))) ,f"\033[0;96m{lista[g]['Saldo']} gol(s)\033[m")


while True:
    per2 = int(input("\nQuer ver as estatisticas de qual jogador ? (0 para parar)"))
    if per2 == 0:
        break
    while per2 > len(lista) or per2 < 0:
        per2 = int(input(f"Por favor, digite numeros entre 0 e {len(lista)} (0 para o programa)"))
    if per2 == 0:
        break
    sleep(0.5)

    print(f"\nEstatisticas de \033[0;36m{lista[per2-1]['Nome']}\033[m\n")
    for gols in range(1, len(lista[per2-1]['Gols'])+1):
        print(f"Na partida {gols}, \033[0;95m{lista[per2-1]['Nome']}\033[m fez {lista[per2-1]['Gols'][gols-1]} Gol(s)")

print("\n\033[0;31mFim\033[m")
