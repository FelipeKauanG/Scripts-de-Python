#Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média

#Tente
try:
    #Seu código aqui
    def mediaAluno(num1=0, num2=0):
        """
            Este programa calcula as duas notas de um aluno e faz uma média entre elas
        """
        print(f"Notas: {num1}, {num2}")

        media = (num1 + num2)/2

        if 5 <= (media)/2 <=6:
            print(f"\033[33mMédia {(num1 + num2)/2}\033[m")
        elif (media)/2 > 6:
            print(f"\033[32mMédia {(num1 + num2)/2}\033[m")
        else:
            print(f"\033[31mMédia {(num1 + num2)/2}\033[m")


    mediaAluno(5.5, 2) 

#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')

except Exception:
    print("\033[31mErro desconhecido\033[m")
