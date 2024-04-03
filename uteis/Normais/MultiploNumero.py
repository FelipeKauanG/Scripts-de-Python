while True:
    numero = int(input("Digite o número "))
    total = 0
    for i in range(numero, 1, -1):
        if numero % i == 0:
            total += 1
            print(f"\033[36m{int(numero/i)}x{i} = {numero}\033[m")
    print(f"Ao todo existe {total} múltiplos de {numero}\n")
