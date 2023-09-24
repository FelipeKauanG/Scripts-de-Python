from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from copy import deepcopy
from selenium.webdriver.support.ui import WebDriverWait

ra = '107058875'
data = "23/06/2003"
digito = '1'
driver = webdriver.Edge(r"consulta de RA\WebDriver\msedgedriver.exe")
wait = WebDriverWait(driver, 10)
arte = []
total = []
anos = []
for ano in range(2015, 2022):
    try:
        print(f"Ano de \033[34m{ano}\033[m")
        anos.append(f"{ano}")
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
        print("\n")
        notaBim = {}
        notas_disciplina = []
        for notn in range(1, 13):  # seleciona cada disciplina
            # pega um número de 4 em 4 para selecionar a coluna certa para pegar as notas de cada bimestre
            for bim in range(2, 17, 4):
                bimnot = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                if bimnot in ('10') or bimnot in ('123456789'):
                    print(f"\033[32m{bimnot}\033[m", end=" ")
                    notas_disciplina.append(bimnot)
                else:
                    print("-", end="")
                if bimnot.i
                snumeric():
                    total.append(int(bimnot))
                else:
                    total.append("-")
                    print("", end="")
            print()
    except:
        print("\n\n\n")
        
driver.quit()
notasTotais = []
materias = {}

for i in range(1, len(total) + 1):
    if i % 4 == 0:
        notasTotais.append(total[ i -4:i])
for a in range(0, len(anos)):
    if len(anos) - 8 < a < len(anos) - 3:  # 2015 a 2018
        # print(f"Ano de : {anos[a]}\n{notasTotais[2*a:(2*a)+8]}\n")
        materias[f"ano de {anos[a]}"] = notasTotais[a*8:a*8+8]
    elif len(anos)-3 == a:  # 2019
        materias[f"ano de {anos[a]}"] = notasTotais[32:44]  # 2019
    elif len(anos)-2 == a:  # 2020
        materias[f"ano de {anos[a]}"] = notasTotais[44:55]  # 2020
    elif len(anos)-1 == a:  # 2021
        materias[f"ano de {anos[a]}"] = notasTotais[55:67]  # 2021

for chav, valor in materias.items():
    print(f"Ano de : {chav}\n\t{valor}\n\n\n")
