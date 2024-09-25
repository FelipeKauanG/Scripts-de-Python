from time import sleep

def calcularRaizQuadrada(a=1, b=1, c=1):
    print( "-*"*5 + "CALCULANDO RAIZ QUADRADA" + "-*"*5)
    print()

    """
    :param a: Primeiro valor da equação quadrática, Ax²
    :param b: Segundo valor da equação quadrática, Bx
    :param c: Terceiro e último valor da equação quadrática, C
    :return: Esta função calcula os valores da raiz quadrada
    """


    delta = (b**2) - (4*a*c)
    x1 = ((-b) + (delta ** 0.5)) / 2 + a
    x2 = ((-b) - (delta ** 0.5)) / 2 + a

    if a == 0:
        print(f"Erro, para uma equação ser quadrática, o valor de \033[32mA\033[m nunca pode ser igual a \033[31m0\033[m,"
              f"\nCaso contrário ela seria uma equação de primeiro grau.")

    elif delta < 0:
        print(f"Não será possível calcular o \033[32mdelta\033[m como valor de \033[31m{delta}\033[m, pois é um valor negativo"
              f"\n,tornando impossível de calcular")
    elif delta == 0:
        print(f"\t\tX = ({a}x²) + ({b}x) + ({c})")
        print(f"\t\t\033[32mDelta\033[m = {delta}")
        print(f"\t\tMostrando um único valor pois o \033[32mdelta\033[m vale \033[31m0\033[m: "
              f"\t\t\n X = {x1}")
    elif (delta ** 0.5) %1 == 0:
        print(f"\t\t\033[32;1mRaiz com quadrado perfeito\033[m")
        print(f"\t\tX = ({a}x²) + ({b}x) + ({c})")
        print(f"\t\t\033[32mDelta\033[m = {delta}")
        print()
        print(f"\t\t\033[36mX'\033[m = \033[1m{x1}\033[m")
        print(f'\t\t\033[35mX"\033[m = \033[1m{x2}\033[m''')

    else:
        print(f"\t\t\033[33;1mRaiz quadrada inexata\033[m")
        print(f"\t\tX = ({a}x²) + ({b}x) + ({c})")
        print(f"\t\t\033[32mDelta\033[m = {delta}")
        print()
        print(f"\t\t\033[36mX'\033[m ≈ \033[1m{x1:.3f}...\033[m")
        print(f'\t\t\033[35mX"\033[m ≈ \033[1m{x2:.3f}...\033[m''')



def gerarEquacaoQuadratica(esc=0):

        print(f"(1) -\033[4;3;37m Equação quadrática\033[m com \033[33mraíz inexata\033[m √11 ≈ {11**0.5:.3f}...")
        print(f"(2) -\033[4;3;37m Equação quadrática\033[m com \033[32mquadrado perfeito\033[m √25 = ±5")
        if esc == 0:
            esc = str(input(f"\033[36;1mAssinale a alternativa acima: \033[m"))
        while not esc.isnumeric() and (esc != "1" or esc != "2"):
            esc = str(input(f"\033[36;1mPor favor digite apenas números de 1 a 2: \033[m"))

        from random import randint

        while True:
            if esc == "1":
                a = randint(-15, 15)
                b = randint(-15, 15)
                c = randint(-15, 15)
                delta = (b ** 2) - (4 * a * c)

                while a == 0:
                    a = randint(-15, 15)
                while delta < 0:
                    a = randint(-15, 15)
                    b = randint(-15, 15)
                    c = randint(-15, 15)
                    delta = (b ** 2) - (4 * a * c)

                #while (delta ** 0.5) % 1 == 0:
                #    a = randint(-15, 15)
                #    b = randint(-15, 15)
                #    c = randint(-15, 15)
                #    delta = (b ** 2) - (4 * a * c)

                print(f"\nA = {a}")
                print(f"B = {b}")
                print(f"C = {c}")
                print(type((delta**0.5) % 1))
                
            else:
                True
            sleep(0.1)

gerarEquacaoQuadratica()
