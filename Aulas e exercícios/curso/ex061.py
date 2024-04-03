#Rafaca o desafio 51, lendo o primeiro termo de uma PA,
# mostrando os 10 primeiros termos da progressao aritmetica usando a estrutura while.

termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))

termos = 0

while termos != 10:
    print("\033[0;34m{} → \033[m".format(termo + (termos * razao)), end=" ")
    termos += 1
print("Fim")
