n = 0
joga = 0
z = str(input("\033[0;31mCrie sua senha \033[m"))
nome = str(input("\033[0;34mLogin: \033[m"))

while n != z:
    n = str(input("Digite sua senha "))
    joga += 1

    if joga > 2:
        print("Voce ultrapassou o limite de senha")
    if z == n:
        print("Voce esta logado como {}".format(nome))
print("Fim")
