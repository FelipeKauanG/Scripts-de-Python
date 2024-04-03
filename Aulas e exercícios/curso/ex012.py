#faça um algoritmo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

pr = float(input("Preço de um produto:R$ "))
des = float(input("Porcentagem de desconto: "))
print("Preço normal {:.2f}\n"
      "Preço com desconto {:.2f}".format(pr, pr*(1-(des/100))))
