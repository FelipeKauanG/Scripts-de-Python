#Crie um programa que leia varios numeros inteiros pelo teclado.
#No final da execucao, mostre a media entre todos os valores e qual foi o maior
#e o menor valores lidos. o Programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

resp = "s"
media = ter = 0

while resp in "Ss":
    num = int(input("Digite um numero: "))
    media += num
    ter += 1
    resp = str(input("\nDeseja continuar ? [S/N]")).upper().strip()[0]
    if ter == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print("A media foi {}".format(media/ter, ter))
print("O maior numero foi {} e o menor numero foi {}".format(maior, menor))
