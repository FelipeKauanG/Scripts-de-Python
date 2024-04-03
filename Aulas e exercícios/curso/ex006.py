n1 = int(input("Digite um \033[0;31mvalor\033[m"))

print("""         O se dobro é \033[0;34m{}\033[m;
         o seu triplo é \033[0;36m{}\033[m;
         e sua raíz quadrada é \033[0;31m{:.2f}\033[m""".format(n1*2, n1*3, n1**(1/2)))



