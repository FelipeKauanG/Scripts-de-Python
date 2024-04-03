#escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

#a multa vai custar R$7,00 por cada Km acima do limite

vel = float(input("Digite a velocidade do carro: "))
if vel > 80:
    print("Voce foi \033[0;31mmultado\033[m")
    print("Com \033[0;32mR${:.2f}\033[m de multa por estar {:.2f}Km acima do normal".format((vel-80)*7, (vel-80)))
else:
    print("Velocidade normal...")