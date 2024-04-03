#Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de
#futebol, na ordem de colocacao. Depois mostre:

#A) Apenas os 5 primeiros colocados.
#B) Os ultimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabetica.
#D) Em que posicao na tabela esta o time da chapecoense.

times = "Palmeiras", "Internacional", "Fluminense", "Flamengo",\
    "Corinthians", "Athletico-PR", "Atletico-MG", "América-MG",\
    "Goiás", "Botafogo", "Santos", "Bragantino", "Sao Paulo",\
    "Fortaleza", "Ceara", "Coritiba", "Avai", "Cuiaba",\
    "Atletico-GO", "Juventude"

print(f"Os cinco primeiros times da tabela sao \n\033[0;34m{times[:5]}\033[m")
print("-=-"*15)
print(f"Os quatro ultimos colocados da tabela sao \n\033[0;32m{times[-4:]}\033[m")
print("-=-"*15)
print(f"Os times em ordem alfabetica sao \n\033[0;36m{sorted(times)}\033[m")
print("-=-"*15)
print("Chapecoence esta na Serie B em 14")
print("-=-"*15)
print("\n\n\n\033[8;34;40;50m21/09/2022\033[m")
