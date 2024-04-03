velocidade = float(input("Qual e a velocidade atual do carro: "))
if velocidade > 80:
    print("Multado, voce excedeu o limite permitido de 80km/h! ")
    multa = (velocidade - 80)*7
    print("Voce deve pegar uma multa de R${:.2f}".format(multa))
    print("Tenha um bom dia, dirija com seguranca")
