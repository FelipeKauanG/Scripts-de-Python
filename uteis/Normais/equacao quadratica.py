a = int(input("valor de A: "))
b = int(input("Valor de B: "))  # valores de a,b,c
c = int(input("Valor de C: "))
d = ((b**2)-4*a*c) #delta
raiz = d**(1/2) #raiz quadrada de delta

print("""O delta vale {}\n
      x1 vale: {}\n
      x2 vale: {}""".format(d, (-b + raiz) / (2 * a), (-b - raiz) / (2 * a)))
