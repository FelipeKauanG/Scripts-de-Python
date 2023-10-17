from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg # pip install PySimpleGUI
# DarkTeal12
import re # importe o módulo re para expressões regulares

def valida_ra(ra):
    return re.match(r"^\d{9}$", ra) is not None

def valida_data(data):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", data) is not None

sg.theme("DarkTeal12")

# Faz o layout do programa
layout = [
    [sg.Text("Insira seu RA")],
    [sg.InputText(key="ra", tooltip="(123456789)" ,enable_events=True), sg.Text("", size=(10, 1), key="ra_validacao")],
    [sg.Text("Data de Nascimento")],
    [sg.InputText(key="data",enable_events=True), sg.Text("", size=(10, 1), key="data_validacao")],
    [sg.Text("Dígito")],
    [sg.InputText(key="digito")],
    [sg.Button("OK") ,sg.Button("Cancelar")],
    
]

window = sg.Window("Caçador de RA", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
 
 
    if event == "OK":
        ra = values["ra"]
        data = values["data"]
        digito = values["digito"]
        
        
        if not ra or not data or not digito:
            sg.popup_error("Preencha todos os campos antes de continuar.")
        elif not valida_ra(ra) or not valida_data(data):
            sg.popup_error("Verifique os campos RA e Data de Nascimento.")
        else:
            window.close()
            
            
        if not valida_ra(ra):
            window["ra_validacao"].Update("RA inválido")
        else:
            window["ra_validacao"].Update("")
            
            
        if not valida_data(data):
            window["data_validacao"].Update("Data inválida")
        else:
            window["data_validacao"].Update("")
            
            
        if valida_ra(ra) and valida_data(data):
            print("RA:", ra)
            print("DAta e nascimento", data)
            print("Dígito", digito)
            
            
        iniAno = int(input("Quantos anos você completou ou vai completar o ensino médio? "))
        
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 7) # Tempo de espera do webdriver
        pontos = 0 # Pontos totais
        num = []
        driver.get(f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={int(data[6:])+iniAno-2}")
        
        nome = str(wait.until(EC.presence_of_all_elements_located((By.XPATH, f"/html/body/div/div/div[2]/div/div/div[2]")))[0].text).title()
        
        documento = "consulta de RA/VerRAs/tabela.txt"
        
        with open(documento, "+a", encoding="utf-8") as tabela:
            tabela.write(f"{nome}\n\n\n")
        tabela.close()
        print(str(nome).title())
        #with open("consulta de RA/VerRAs/tabela.txt", "a+", encoding="utf-8") as texto:
        #    texto.write("")
        
        for ano in range(int(data[6:])+iniAno-6, int(data[6:])+iniAno+1):
            try:
                try:
                    print(f"Ano de \033[34m{ano}\033[m")
                    driver.get(
                        f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa={'000'+ra}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={ano}"),
                    print("\n")

                    tabelaNotas = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"/html/body/div/div/div[4]/table")))[0].text
                    
                    
                    
                    with open(documento, "a+", encoding="utf-8") as tabela:
                        tabela.write(f"Ano: {ano}\n{tabelaNotas}\n\n")
                    
                    
                    
                    for notn in range(1, 13):
                        for bim in range(2, 15, 4):
                            bimnot = wait.until(EC.presence_of_all_elements_located((By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
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