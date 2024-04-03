r1 = float(input("\033[0;31mPrimeiro seguimento:\033[m "))
r2 = float(input("\033[0;33mSegundo segmento:\033[m "))
r3 = float(input("\033[0;32-mTerceiro segmento:\033[m "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar triangulo", end=" ")
    if r1 == r2 == r3:
        print("EQUILATERO!")
    if r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISOSCELES!")
else:
    print("Os segmentos acima nao podem formar um triangulo")
