#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Nome completo: ")).strip()
print("\033[0;34mSeu nome tem 'Silva'\033[m \n\n{}".format("silva" in nome.lower()))
