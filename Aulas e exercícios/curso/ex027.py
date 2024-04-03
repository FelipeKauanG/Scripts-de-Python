#Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = str(input("\033[0;33mQual e o seu nome:\033[m ")).strip()
pri = nome.find(" ")
ult = nome.rfind(" ")

print("\033[0;34mOla, prazer em te conhecer: \033[0;31m{}\033[m\n"
     "Seu primeiro nome e: {}\n"
     "Seu ultimo nome e: {}\033[m".format(nome.title(), nome[:pri], nome[ult:]))
