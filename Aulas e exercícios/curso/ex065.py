#Crie um programa que leia varios numeros intewiros pelo teclado.
#No final da execucao, mostre a media entre todos os valores e qual foi o maior
#e o menor valores lidos. o Programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

ter = 0
media = 0
per = "s"
while per != "n":
    num = int(input("Valor: "))
    per = str(input("Deseja continuar a digitar valores [S/N] ?")).lower().strip()
    media += num
    ter += 1
print("Fim")
print("Media foi de {:.2f}".format(media / ter))
