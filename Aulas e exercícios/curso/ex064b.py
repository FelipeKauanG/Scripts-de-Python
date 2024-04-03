#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario
#digitar o valor 999, que e a condicao de parada. No final mostre quantos numeros foram digitados e qual
#foi a soma entre eles.
#(Desconsiderando o flag)
num = cont = soma = 0
num = int(input("Digite um numero [999] para parar:"))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um numero [999] para parar:"))
print("Voce digitou {} numeros e a soma entre eles foi {}".format(cont, soma))
