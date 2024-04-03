#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

#Tente
try:
    def calcularArea(larg=0, alt=0):
        """
        Este código calcula a quantidade necessária de tinta e a área total da parede, sabendo que a tinta rende 1L para 2 m².
        O primeiro argumento é da largura, e o segundo argumento é da altura.
        """
        area = larg*alt
        quantLitro = larg*alt/2
        
        print(f"\n\033[1mA área da parede é de\033[m \033[36m{area} m²\033[m")
        print(f"\033[1mUma parede de \033[m\033[32m{larg}m X {alt}m\033[m daria \033[33m{quantLitro:.2f}L\033[m")

    
    calcularArea()


#TRatamento de erros
except KeyboardInterrupt:
    print(f"\033[31mPrograma encerrado com sucesso\033[m")

except NameError:
    print('\033[31mErro de nome, sempre coloque " " quando colocar nomes próprios por gentileza\033[m')


except ModuleNotFoundError:
    print("\033[31mBilbioteca não instalada\033[m")
