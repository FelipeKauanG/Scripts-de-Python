#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input("\033[0;32;40mSalário: \033[m"))
aum = float(input("Aumento em porcentagem: "))

print("\033[0;31mSalário normal:\033[m {}\n"
      "\033[0;32mSalário com aumento:\033[m {:.2f}".format(sal, sal*(1+(aum/100))))
