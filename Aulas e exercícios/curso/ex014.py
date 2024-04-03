#escreva uma temperatura que converte uma temperatura digitada em c e converta para f
n1 = float(input("Temperatura em \033[0;33mC\033[m: "))

print("Temperatura em \033[0;31mF:\033[m {:.2f}\n"
      "Temperatura em \033[0;36mK\033[m: {:.2f}".format(n1*1.8+32, n1 + 273.15))
