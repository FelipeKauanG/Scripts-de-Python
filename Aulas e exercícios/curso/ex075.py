#Deselvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

#A) Quantas vezes apareceu o valor 9
#B) Em que posicao foi digitado o primeiro valor 3.
#C) Quais foram os numeros pares.

valores = int(input("Digite o primeiro valor: ")), int(input("Digite o segundo valor: ")),\
          int(input("Digite o terceiro valor")), int(input("Digite o quarto valor: "))

print(f"{valores[0]} {valores[1]} {valores[2]} {valores[3]}")
print(f"\nO numero '9' apareceu {valores.count(9)} vez(es)")
if valores.count(3) == 0:
    print("Nao apareceu \033[0;31mnenhuma\033[m vez o valor '3'")
else:
    print(f"A posicao do primeiro valor '3' esta na \033[0;32m{valores.index(3)+1}\033[m posicao ")

print(f"Os valores pares sao: ")
for cont in range(0, 4):
    if valores[cont] % 2 == 0:
        print(valores[cont], end=" ")
