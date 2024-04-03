#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaç~es possíveis sobre ele.abs

try:
    def mostrarTipoPrimitivo(string="Sem valor declarado"):

        """
        apenas basta colocar um valor na função mostrarTipoPrimitivo que o programa irá resolver se não tiver erro, ele tem um tratamento de erros.
        """
        tipo = type(string)
        print()
        if tipo == type("a"):
            print(f"\033[34mO tipo primitivo de {string} é {type(string)}\033[m")
            print(f"\033[36mEle é uma cadeia de caracteres\033[m")
        elif tipo == type(1):
            print(f"\033[34mO tipo primitivo de {string} é {type(string)}\033[m")
            print(f"\033[36mEle é um valor inteiro!\033[m")
        elif tipo == type(1.1):
            print(f"\033[34mO tipo primitivo de {string} é {type(string)}\033[m")
            print(f"\033[36mEle é um valor que contém vírgula!\033[m")
        elif tipo == type(True):
            print(f"\033[34mO tipo primitivo de {string} é {type(string)}\033[m")
            print(f"\033[36mEle é um valor booleano (verdadeiro ou falso)\033[m")


    mostrarTipoPrimitivo(1)

except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")