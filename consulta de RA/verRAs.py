from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Dados do aluno
ra = '107058875'
data = "23/06/2003"
digito = '1'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7)
pontos = 0
num = []

for ano in range(2015, 2022):
    try:
        try:
            print(f"\033[34mAno de {ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}")
            print("\n")

            for notn in range(1, 13):
                for bim in range(2, 15, 4):
                    bimnot = wait.until(EC.presence_of_all_elements_located(
                        (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                    cleaned_bimnot = str(bimnot).replace(" ", "").replace("-","")
                    
                    if cleaned_bimnot.isdigit():
                        pontos += int(bimnot)
                        num.append(bimnot)
                        print(f"{bimnot}", end=" ")
                print()
        except Exception:
            print("\n\n\n")
    except Exception:
        print(f"Não consegui ver este boletim!")
driver.quit()
print(f"Pontos totais: {pontos}\nMédia do aluno total: {pontos / len(num):.2f}")
