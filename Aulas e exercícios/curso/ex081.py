#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, mostre:

#A) Quantos numeros foram digitados.

#B) A lista de valores, ordenada de forma decrescente.

#C) Se o valor 5 foi digitado e esta ou nao na lista.

lista = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    per = str(input("Quer continuar ?")).lower().strip()
    if per not in "sn":
        per = str(input("Quer continuar ?")).lower().strip()
    if per == "n":
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} numeros")
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 nao faz parte da lista")
