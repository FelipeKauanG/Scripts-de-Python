#desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preco da passagem, cobrando R$0,50 por Km para viagem de ate 200Km,
# e R$0,45 para viagens mais longas

km = float(input("Distancia da viagem: "))

if km > 200:
    print("Preco da passagem total: \033[0;32mR${:.2f}\033[m:".format(((km-200)*0.45)+100))
else:
    print("Preco da passagem total: \033[0;32mR${:.2f}\033[m".format(km*0.5))
