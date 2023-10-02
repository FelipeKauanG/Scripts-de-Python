from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
total = 0
texto = open("R.AsCaçados.txt", "a")
log = open("log.txt", "a")
for raNum in range(106190323, 107409999):
#for raNum in range(107058872, 107058877):
    try: 
        agora = datetime.datetime.now()
        agora_formatado = agora.strftime("%Y-%m-%d %H:%M:%S")
        ano = "2019"
        digito = 1
        #raNum = "000107058871"
        data = "22/06/2004"
        driver = webdriver.Chrome()
        driver.get(
            f"https://sed.educacao.sp.gov.br/Boletim/GerarBoletimUnificadoExterno?nrRa=000{+raNum}&nrDigRa={digito}&dsUfRa=SP&dtNascimento={data}&nrAnoLetivo={ano}")
        wait = WebDriverWait(driver, 2)
        nome = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/div[2]")))
        #print(f"\033[32m{nome.text}\033[m")
        #print(f"\033[32m{raNum}\033[m")
        texto.writelines(f"Nome: {nome.text}, RA: {raNum},Data: {data}, Digito: {digito}\n")
        texto.flush()

    except:
        #print(f"\033[31mRA de 000{raNum} Não deu certo\033[m")
        log.writelines(f"RA: {raNum}, Digito {digito}, Data do boletim: {data} Tempo: {agora_formatado}\n")
        log.flush()

print("\033[36mFim do programa\033[m")
