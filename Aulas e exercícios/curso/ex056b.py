somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher = 0
for p in range(1, 5):
    print("---- {} ---- Pessoa".format(p))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in ("Mn"):
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print("A media de idade do grupo e de {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("Ao todo sao {} mulheres com menos de 20 anos".format(totmulher))
