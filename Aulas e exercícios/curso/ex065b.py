# Crie um programa que leia varios numeros inteiros pelo teclado.
# No final da execucao, mostre a media entre
# todos os valores lidos.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

resp = "S"
soma = quant = media = 0
while resp in "Ss":

    num = int(input("Digite um numero: "))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Quer continuar ? [S/N]")).upper().strip()[0]
media = soma / quant
print("Voce digitou {} numeros e a media foi {}".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
