# A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com sua idade:
from datetime import date
idade = int(input("qual \033[0;37mano\033[m voce nasceu ?"))

cate = date.today().year - idade
print("Sua idade {}".format(cate))
if cate <= 9:
    print("\033[0;36mCategoria Mirim\033[m") #abaixo de 9 anos
elif cate <= 14:
    print("\033[0;34mCategoria Infantil\033[m") #14 anos
elif cate <= 19:
    print("\033[0;33mCategoria Junior\033[m") #19 anos
elif cate <= 20:
    print("\033[0;31mCategoria Senior\033[m") #20 anos
else:
    print("\033[0;35mCategoria Master\033[m") #35 acima de 20 anos
