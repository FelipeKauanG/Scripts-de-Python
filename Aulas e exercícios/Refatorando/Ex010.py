#Crie um program que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere $1 = R$4.98

#Tente
try:
    #Seu código aqui
    
    def converterDolarParaReal(num=0):
        """
            Esta função converte o real para o dólar
        """
        print(f"\033[1mVocê pode comprar\033[m \033[32m${ num / 4.98 :.2f}\033[m")

    converterDolarParaReal(19.88)

#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')


except ModuleNotFoundError:
    print(f"\033[31mBilbioteca não instalada\033[m")

