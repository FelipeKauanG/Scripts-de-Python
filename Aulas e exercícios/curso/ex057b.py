sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0]


while sexo not in "MFmf": #enquanto nao estiver MFmf em sexo
    sexo = str(input("Dados invalidos, por favor informe o seu sexo: ")).strip().upper()[0] #ler apenas a primeira letra no programa
print("Sexo {} registrado com sucesso".format(sexo)) #sexo tal registrado com sucesso

