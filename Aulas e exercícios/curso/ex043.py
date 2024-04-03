# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# abaixo do peso: 18,5
# entre 18 e 25: peso ideal
# de 25 a 30: sobrepeso
# de 30 a 40: obesidade
# acima de 40: obesidade morbida

alt = float(input("Altura em M: "))
peso = float(input("Peso em KG: "))

imc = peso/(alt**2)

print("IMC DE {:.2f}".format(imc))
if imc < 18.5:
    print("\033[0;36mAbaixo do peso\033[m")
elif 18.5 < imc <= 25:
    print("\033[0;32mPeso ideal\033[m")
elif 25 < imc <= 30:
    print("\033[0;33mSobrepeso\033[m")
elif 30 < imc <= 40:
    print("\033[0;31mObesidade\033[m")
elif imc > 40:
    print("\033[0;35mObesidade morbida\033[m")
    