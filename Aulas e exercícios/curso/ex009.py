#faça um programa que leia um número inteiro equalquer e mostre na tela a sua tabuada

n1 = int(input("Qual é o seu valor numérico: ?"))
print("""\033[0;31mTabuada\033[m de {}
          
        {}
        {}
        {}
        {}
        {}
        {}
        {}
        {}
        {}
        {}""".format(n1, n1*1, n1*2, n1*3, n1*4, n1*5,n1*6, n1*7, n1*8, n1*9, n1*10))
