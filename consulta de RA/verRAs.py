from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ra = str(input("RA do aluno (123456789): ")).strip()
data = str(input("Data de nascimento (01 02 2003): ")).strip()
digito = str(input("Dígito verificador (um digito): ")).strip()
data.replace(" ", "/").strip()
iniAno = int(input("Qual idade você tinha no 5º ano ?"))
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7)
pontos = 0
num = []
for ano in range(int(data[5:])+iniAno, int(data[5:])+iniAno+7):
    try:
        try:
            print(f"Ano de \033[34m{ano}\033[m")
            driver.get(
                f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={000+ano}"),
            print("\n")
 
            for notn in range(1, 13):
                for bim in range(2, 15, 4):
                    bimnot = wait.until(EC.presence_of_all_elements_located(
                    (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                    if bimnot.isdigit:
                        pontos += int(bimnot)
                        num.append(bimnot)
                        print(f"{bimnot}", end=" ")

                print()
        except:
            print("\n\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()
print(f"\033[33mPontos totais {pontos}\033[m"
      f"\n\033[32mMédia do aluno total: {pontos/int(num.count()):.2f}")
