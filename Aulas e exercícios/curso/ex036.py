# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestacao mensal, sabendo que ela nao pode exercer 30% do salario ou entao o emprestimo sera negado.
casa = float(input("Valor do imovel: "))
sal = float(input("Qual o seu salario para o emprestimo: "))
ano = int(input("Quantos anos voce ira pagar seu imovel ?"))

prestacao = casa / (ano*12)

if prestacao > sal * 0.3:
    print("\033[0;31mEmprestimo NEGADO!\033[m,pois a prestacao sera de R${:.2f}\n"
          "e isso e maior do que R${:.2f}".format(prestacao, sal*0.3))
else:
    print("\033[0;32mEmprestimo ACEITO!!\033[m, pois a prestacao sera de R${:.2f}\n"
          "e isso e menor do que R${:.2f}.".format(prestacao, sal*0.3))
#print(prestacao)
