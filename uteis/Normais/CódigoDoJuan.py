print("\n>>>>>> Olá Para começarmos especifique o valor de quantas empresas estão sendo alocadas no sistema sendo separadas por: \n\nGrande empresa \nMedia empresa \nPequena empresa \nMicro empresa\n")


empresa_grande = int(input("Primeiro valor: "))
empresa_media = int(input("Segundo valor: "))
empresa_pequena = int(input("Terceiro valor: "))
micro_empresa = int(input("Quarto valor: "))

maior_empresa = ""
maior_numero_funcionarios = 0

opcao = 5

while opcao != 0:
    print("""
        [1] Empresa Grande
        [2] Empresa Media
        [3] Empresa Pequena
        [4] Micro Empresa""")
    opcao = int(input("Qual é a sua opção ?"))

    if opcao == 1:
        print("Digite o número de funcionários da empresa grande: ")

        numeros_de_funcionarios_empresa_grande = int(input("Número de funcionários da empresa Grande: "))

        if numeros_de_funcionarios_empresa_grande > maior_numero_funcionarios:
            maior_numero_funcionarios = numeros_de_funcionarios_empresa_grande
            maior_empresa = "Grande Empresa"
            
    elif opcao == 2:
        print("Digite o número de funcionários da empresa média: ")

        numeros_de_funcionarios_empresa_media = int(input("Número de funcionários da empresa Média: "))

        if numeros_de_funcionarios_empresa_media > maior_numero_funcionarios:
            maior_numero_funcionarios = numeros_de_funcionarios_empresa_media
            maior_empresa = "Media Empresa"
            
    elif opcao == 3:
        print("Digite o número de funcionários da empresa pequena: ")

        numeros_de_funcionarios_empresa_pequena = int(input("Número de funcionários da empresa pequena: "))

        if numeros_de_funcionarios_empresa_pequena > maior_numero_funcionarios:
            maior_numero_funcionarios = numeros_de_funcionarios_empresa_pequena
            maior_empresa = "pequena Empresa"
            
    elif opcao == 4:
        print("Digite o número de funcionários da empresa micro: ")

        numeros_de_funcionarios_empresa_micro = int(input("Número de funcionários da micro empresa: "))

        if numeros_de_funcionarios_empresa_micro > maior_numero_funcionarios:
            maior_numero_funcionarios = numeros_de_funcionarios_empresa_micro
            maior_empresa = "micro Empresa"
    else:
        print("Você digitou um valor inválido. Insira um valor válido")
    print("=-="*20)

    print(f"A maior empresa é {maior_empresa} com {maior_numero_funcionarios} funcionários.")
    print("Você finaliou o programa, até mais :)")
