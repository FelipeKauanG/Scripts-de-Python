from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import os


xpath = "/html/body/div[6]/div/div[8]/div/div[5]/div/div/div[2]/div/div/input[2]//div"



endereço = os.path.abspath(r"C:\Users\Felipe Kauan\Desktop\Object models near point 2712, -1740.html")


driver = webdriver.Chrome()
driver.get(endereço)

className = "mp-item"

elementos = driver.find_elements(By.CLASS_NAME,className)

DFFs = []


for elemento in elementos:
    nome = elemento.get_attribute("data-name")
    DFFs.append(nome)

print(f"Tem {len(elementos)} ao todo no site")

print(DFFs)
    

#print(f"\033[34mTem {len()} itens\033[m")

driver.quit()

