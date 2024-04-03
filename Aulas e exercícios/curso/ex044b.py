print("{} LOJAS GUANABARA")
preco = float(input("Precos das compras: R$ "))
print("""FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/ cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao """)
opcao = int(input("Qual e a opcao? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print("Sua compra de R${:.2f}n vai custar R${} no final".format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 /100)
    print("Sua compra de R${:.2f}n vai custar R${} no final".format(preco, total))

elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS)".format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input("Quantas parcelas ?"))
    parcela = total / totalparc
    print("Sua compra sera parcelada em {} vezes de R${:.2f}".format(totalparc, parcela))
else:
    total = 0
    print("Opcao invalidade de pagamento")
print("Sua compra de R${:.2f}n vai custar R${} no final".format(preco, preco))

