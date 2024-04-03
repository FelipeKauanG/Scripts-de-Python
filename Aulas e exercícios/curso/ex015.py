#escreva um exercicio que pergunte a quantidade de km percorridos p
# or um carro alugado e a quantidade de dias pelos quais ele foi alugadio,
# calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15km rodado.

n2 = float(input("Quantidade de dias: "))
n1 = int(input("Quantidade de quilometros: "))

print("O valor total a pagar e: \033[0;32mR${:.2f}\033[m".format(n1*0.15 + n2*60))
