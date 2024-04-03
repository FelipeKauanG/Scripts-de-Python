while True:
    from random import sample
    valores = []
    per = []
    for c in range(0, 6):
        per.append(int(input("Digite um numero da Mega Sena: ")))
    for i in range(1, 61):
        valores.append(i)
    sorteado = sample(valores, k=6)
    sorteado.sort(reverse=False)
    print(f"Os valores que voce escolheu foram: {sorted(per)}")
    print(f"Os valores da Mega Sena foram:    {sorteado}")
    per = str(input("Quer continuar ?")).lower().strip()
    if per not in "sn":
        per = str(input("Quer continuar ?")).lower().strip()
    if per in "n":
        break
    print("-=-" * 15)
print("FIM")
