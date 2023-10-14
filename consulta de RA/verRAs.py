from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg # pip install PySimpleGUI
# DarkTeal12

sg.theme("DarkTeal12")

# Faz o layout do programa
layout = [[sg.Text("RA do aluno (123456789)")], [sg.Text("Data de nascimento (01 02 2003)")], [sg.Text("Digito do aluno")],[sg.Button("Cancelar")]]
janela = sg.Window("Caçador de notas", layout, size=(600, 200))
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
        break




ra = str(input("RA do aluno (123456789): ")).strip() # seu Registro do Aluno
data = str(input("Data de nascimento (01 02 2003): ")).strip() # sua data de nascimento
digito = str(input("Dígito verificador (um digito): ")).strip()
data.replace(" ", "/").strip()
iniAno = int(input("Qual idade você tinha no 5º ano ? ")) 
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 7) # Tempo de espera do webdriver
pontos = 0 # Pontos totais
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
                    if bimnot.isdigit():
                        pontos += int(bimnot)
                        num.append(bimnot)
                        print(f"{bimnot}", end=" ")
                print()
        except:
            print("\n\n\n")
    except:
        print(f"\033[34m\033Não consegui ver este boletim![m")
driver.quit()
print(f"A média total do aluno é de : \033[31m{pontos/len(num):.2f}\033[m com {len(num)} notas totais, {pontos} pontos.")
