distancia = float(input("Qual e a distancia da sua viagem"))

print("Voce esta prestes a fazer uma viagem de {}Km".format(distancia))
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print("E o preco da sua passagem sera de R${:.2f}".format(preco))
