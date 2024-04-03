#Faça um programa que leia a
# largura e a altura de uma parede em metros. calcula a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, rende 2m².

lar = float(input("Qual é a \033[0;31mlargura\033[m em metros ?"))
alt = float(input("Qual é a \033[0;32maltura\033[m em metros ?"))

print("Largura: {}\n"
      "Altura: {}\n"
      "Serão necessários \033[1;36m{:.2f}\033[m Litros de tinta.\n"
      "Essa tinta rende 2m².".format(lar, alt, (lar*alt)/2))
