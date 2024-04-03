#Faca um programa que leia cinco valores numericos e guarde em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista.

lista = [int(input("Digite um valor")), int(input("Digite outro valor: ")),
         int(input("Digite outro um valor: ")), int(input("Digite mais um valor: ")),
         int(input("Digite o ultimo valor: "))]


print(f"O maior valor foi {max(lista)} na posicao {lista.index(max(lista))+1}"
      f"\nO menor valor foi {min(lista)}, na posicao {lista.index(min(lista))+1} ")
