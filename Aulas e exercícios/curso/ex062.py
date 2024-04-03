#Melhore o desafio 061, perguntando para o usuario se ele quer mais alguns termos.
#O programa encerra quando ele quer mostrar 0 termos.
print("Razao Aritmetica")

termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
print("-=-"*15)
ter = 0
per = 1
totaltermos = 10

while per != 0:
    termos = 0
    while termos != totaltermos:
        print("\033[0;34m{}\033[m".format(termo + (termos * razao)), end=" ")
        termos += 1
    per = int(input("\n\nQuer adicionar mais termos ? Quantos ?; "
                    "\n(use \033[0;36m0\033[m para finalizar o programa.)"))
    totaltermos += per
print("\n\033[0;31mPrograma finalizado\033[m")
