# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$1.250,00, calcule um aumento de 10%.
#para os inferiores ou iguais, o aumentio e de 15%

sal = float(input("Qual e o seu salario ?"))

if sal >= 1250:
    print("Seu aumento de salario seria de \033[0;32mR${:.2f}\033[m".format(sal * 1.1))
else:
    print("Seu salario aumentado e de \033[0;32mR${:.2f}\033[m".format(sal * 1.15))
