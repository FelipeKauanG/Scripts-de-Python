#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

#Tente
try:
    def calcularDesconto():
        preco = float(input("Digite o valor do Preço: "))
        desconto = preco * 0.95
        print(f"\033[mPreço atual de:\033[m \033[31mR${preco:.2f}\33[m")
        print(f"\033[1mPreço com desconto:\033[m \033[35mR${desconto:.2f}\033[m")
        

    calcularDesconto()
#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')


except ModuleNotFoundError:
    print("\033[31mBilbioteca não instalada\033[m")
