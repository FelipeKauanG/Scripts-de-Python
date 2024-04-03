#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preco normal e condicao de pagamentos:
#a vista dinheiro/cheque: 10% de desconto
#a vista no cartao: 5% de desconto
#em ate 2x no cartao: preco normal
#3x ou mais no cartao: 20% de juros

from time import sleep
print("\033[0;32mLOJA GUANABARA\033[m")
val = float(input("\033[4;34mValor a ser pago:\033[m "))

esc = float(input("\033[0;36mDigite 1\033[m para dinheiro ou cheque: \n"
                  "\033[0;36mDigite 2\033[m para pagamento a vista no cartao: \n"
                  "\033[0;36mDigite 3\033[m para 2x no Cartao: \n"
                  "\033[0;36mDigite 4\033[m para 3x no Cartao: "))


if esc == 1:

    print("\n\033[0;32mProcessando...\033[m")
    sleep(1.5)
    print("\nO valor a ser pago pelo cheque ou dinheiro e de \033[0;32mR${}\033[m\n"
          "\033[0;32mcom 10% de desconto\033[m".format(val*0.90))
elif esc == 2:

    print("\n\033[0;32mProcessando...\033[m")
    sleep(1.5)
    print("\nO valor a vista no cartao e de \033[0;32mR${}\033[m\n"
          "com \033[0;32m5% de desconto\033[m".format(val*0.95))
elif esc == 3:

    print("\n\033[0;32mProcessando...\033[m")
    sleep(1.5)
    print("\nPreco normal em 2x no cartao e de \033[0;32mR${}\033[m".format(val))
elif esc == 4:

    print("\n\033[;032mProcessando...\033[m")
    sleep(1.5)
    print("\nO valor a pagar no cartao em 3x e de \033[0;32mR${}\033[m\n"
          "com \033[0;31m20% de juros\033[m".format(val*1.2))
else:
    print("\033[0;31mValor invalido!!\033[m")
