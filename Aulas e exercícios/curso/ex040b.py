nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print("Tirando {:.1f} e {:.1f}, a media do aluno e {:.1f}".format(nota1, nota2, media))

if 5 <= media < 7:
    print("O aluno esta em recuperacao")
elif media < 5:
    print("O aluno esta reprovado")
elif media >= 7:
    print("O aluno esta aprovado")