# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Tente
try:
    def aumentarSalario():
        salario = float(input("Salário atual: (R$)"))
        aumento = salario*1.15
        return print(f"\033[34mSeu salário com aumento é de:\033[m \033[32mR${aumento:.2f}\033[m")

    aumentarSalario()

#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')


except ModuleNotFoundError:
    print("\033[31mBilbioteca não instalada\033[m")
    

except ValueError:
    print("\033[31mTalvez você tenha colocado uma valor com vírgula em um input ou em algum outro lugar como 1920,54, mas você precisa colocar com ponto 1920.54\033[m")