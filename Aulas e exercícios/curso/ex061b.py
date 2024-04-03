#Rafaca o desafio 51, lendo o primeiro termo de uma PA,
# mostrando os 10 primeiros termos da progressao aritmetica usando a estrutura while.

print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao da PA:"))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} → ".format(termo), end="")
    termo += razao
    cont += 1
print("Fim")
