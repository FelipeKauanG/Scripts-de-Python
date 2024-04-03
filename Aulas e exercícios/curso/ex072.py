#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
#Seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

contagem = "Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", \
           "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze",\
           "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte"

num = int(input("Qual numero quer mostrar por extenso  entre 0 e 20?"))
if num > 20 or num < 0:
    print("Tente novamente")
else:
    print(f"{contagem[num]}")
