#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista.
#Ja na posicao correta de insercao [sem usar o sort()].
#No final, mostre a lista ordenada na tela.

try:
    valores = []
    valoresOrganizados = []
    for i in range(1, 6):
        num = str(input(f"\033[36m({len(valores)+1})Valor numérico: \033[m"))
        while not num.isnumeric() or not (num % 1 != 0):
            num = str(input(f"\033[36m({len(valores)+1})Por gentileza, insira apenas valores reais: \033[m "))
        valores.append(num)
    print(f"\033[31mValores anteriores{valores}\033[m")
    for i in range(0, 5):
        menorValor = 0
        for num in valores:
            if valores.index(num) == 0:
                menorValor = num
            else:
                if float(menorValor) > float(num):
                    menorValor = num
        valoresOrganizados.append(menorValor)
        valores.remove(menorValor)
    print(f"\033[34mValores atualizados {valoresOrganizados}\033[m")

except KeyboardInterrupt:
    print(f"\n\033[31mPrograma finalizado ^.^\n")
