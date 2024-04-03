#Copie e cole essa estrutura no seu código apra tratamento de erros.

#Tente
try:
    #Seu código aqui
    print("Hello World")


#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')


except ModuleNotFoundError:
    print("\033[31mBilbioteca não instalada\033[m")

except ValueError():
    print("\033[31mTalvez você tenha colocado uma valor com vírgula em um input ou em algum outro lugar como 1920,54, mas você precisa colocar com ponto 1920.54\033[m")