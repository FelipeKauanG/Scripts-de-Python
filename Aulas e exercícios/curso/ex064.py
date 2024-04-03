#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario
#digitar o valor 999, que e a condicao de parada. No final mostre quantos numeros foram digitados e qual
#foi a soma entre eles.
#(Desconsiderando o flag)

print("")
res = 0
c = 1
num = 0
while c != 999:
    c = int(input("Digite um numero: \n se quiser parar o programa, digite (999): "))
    res += c
    num += 1

print("\nA soma de todos os numeros que voce digitou e igual a \033[0;35m{}\033[m".format(res-999))
print("\nForam \033[0;34m{}\033[m numeros que foram digitados".format(num-1))
