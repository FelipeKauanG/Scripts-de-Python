total = totmil = menor = cont = 0
barato = " "

while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco R$"))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "

    while resp not in "SN":
        resp = str(input("Quer continuar ? [S/N] ")).upper().strip()
    if resp == "N":
        break


print("-=-"*15)
print("Fim do programa")
print(f"O total da compra foi R${total}")
print(f"Temos {totmil} custando mais de R$1000")
print(f"O produto mais barato foi {barato} que custa R${menor}")
