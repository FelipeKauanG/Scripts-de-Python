#Melhore o desafio 061, perguntando para o usuario se ele quer mais alguns termos.
#O programa encerra quando ele quer mostrar 0 termos.

print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} → ".format(termo), end="")
        termo += razao
        cont += 1
    print("Fim")
    mais = int(input("Quantos termos voce quwer mostrar a mais ?"))
print("Progressao finalizada com {} termos mostrados".format(total))
