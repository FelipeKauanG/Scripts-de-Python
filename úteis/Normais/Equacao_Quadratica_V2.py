valores = int(input("Valor de A: ")), int(input("Valor de B: ")), int(input("Valor de C: "))
#valores = 1, 7, 12
if valores[0] == 0:
    print("Valor de A nao pode ser 0, pois ela se torna uma equacao de primeiro grau")
delta = (valores[1]**2) - 4*valores[0] * valores[2]

if delta < 0:
    print(f"Delta com valor negativo '{delta}'")
elif delta ** 0.5 % 1 > 0:
    print(f"Delta com raiz nao exata '{delta}'")
else:
    if (-valores[1]-delta**0.5)/(2*valores[0]) == (-valores[1]+delta**0.5)/(2*valores[0]):
        print(f"X0 vale {(-valores[1]+delta**0.5)/(2*valores[0]):.2f}")
    else:
        print(f"""X1 vale {(-valores[1]-delta**0.5)/(2*valores[0])}
X2' vale {(-valores[1]+delta**0.5)/(2*valores[0]):.2f}""")
