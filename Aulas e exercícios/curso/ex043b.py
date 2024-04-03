peso = float(input("Qual e o seu peso ?"))
altura = float(input("Qual e a sua altura ?"))
imc = peso/(altura ** 2)
print("O IMC DESSA PESSOA E DE {:.1f}".format(imc))

if imc < 18.5:
    print("Voce esta a baixo do peso normal!")
elif 18.5 <= imc <= 25:
    print("Parabens, voce esta na faixa de peso normal")
elif 25 <= imc < 30:
    print("Voce esta com sobrepeso")
elif 30 <= imc < 40:
    print("Voce esta com OBESIDADE")
elif imc >= 40:
    print("Voce esta com obesidade morbida, cuidado!")
