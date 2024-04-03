#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos, na sequencia.
#No final, mostre uma listagem de precos. organizando os dados em forma tabular.

print("-=-"*15)
print("Listagem de precos")
print("-=-"*15)

listagem = "Oleo", 6.8, "Caneta Stabilo", 7.5, "Frango (kg)", 32.98, "Minecraft", 125.5, "Bloco de notas", 16,\
           "Celular", 1500, "Estojo", 4.6, "Fone de ouvido", 26.7, "Carregador", 8, "Mouse", 90, "Teclado", 250,\
           "Computador", 5000, "Cubo magico", 25

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(listagem[i], end="")
        print("." * (40-len(listagem[i])), end="")
        print(f"R${i+1:.2f}")
