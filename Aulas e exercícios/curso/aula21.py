#def fatorial(num=1):
#    f = 1
#    for c in range(num, 0, -1):
#        f *= c
#    return f
#
#
#f1 = fatorial(5)
#f2 = fatorial(4)
#f3 = fatorial()
#print(f"Os resultados sao {f1}, {f2} e {f3}")

#def par(n=0):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
#
#
#num = int(input("Digite um numero: "))
#if par(num):
#    print("E par")
#else:
#    print("Nao e par")


#def funcao():
#    n1 = 4
#    print(f"n1 dentro vale {n1}")
#
#
#funcao()
#n1 = 2
#print(f"N1 fora vale {n1}")
#

#def teste(b):
#    a = 8
#    b += 4
#    c = 2
#    print(f"A dentro vale {a}")
#    print(f"B dentro vale {b}")
#    print(f"C dentro vale {c}")
#
#
#a = 5
#teste(a)
#print(f"A fora vale {a}")

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(1, 6, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f"Meus calculos deram {r1}, {r2} e {r3}")
