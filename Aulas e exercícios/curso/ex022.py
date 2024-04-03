# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas

# o nome com todas as letras minusculas

# quantas letras ao todo (sem considerar espacos)

# quantas letras tem o primeiro nome

frase = str(input("Nome completo: ")).strip()
spl = frase.split()
repl = frase.replace(" ", "")

print("{}    \033[0;31m*minusculas\033[m\n"
      "{}    \033[0;32m*MAIUSCULAS\033[m \n"
      "{}    \033[0;33m*Quantidade de letras\033[m\n"
      "{} ".format(frase.lower(), frase.upper(), len(repl), frase.find(" ")))
