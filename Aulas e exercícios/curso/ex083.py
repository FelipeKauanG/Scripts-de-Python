#Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
#Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.

expre = str(input("Expressao matematica: "))
n1 = expre.count("(")
n2 = expre.count(")")
if n1 != n2:
    print("A expressao acima esta errada!")
elif expre in """)(""":
    print("A expressao acima esta errada!")
else:
    print("A expressao acima esta certa!")
