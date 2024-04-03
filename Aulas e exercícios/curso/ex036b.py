casa = float(input("Valor da casa: "))
salario = float(input("Salario do comprador: "))
anos = int(input("Quantos anos de financiamento: "))
prestacao = casa / (anos * 12)
print("Para pagar uma casa de R${:.2f} em {:.2f} anos\n"
      "a prestacao sera de R${:.2f}".format(casa, anos, prestacao))
minimo = salario * 0.3
print("Comparando, tem que pagar R${:.2f} e o minimo e de R${:.2f}".format(prestacao, salario*0.3))

if prestacao <= minimo:
    print("Emprestimo pode ser concedido")
else:
    print("Emprestimo negado")
