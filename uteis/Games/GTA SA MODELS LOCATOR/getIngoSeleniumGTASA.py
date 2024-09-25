from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = str(input("Inserir o link: "))
xpath = "/html/body/div[6]/div/div[8]"

driver = webdriver.Chrome()
driver.get(link)

# Aguardando até que todos os elementos sejam localizados
elementos = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, xpath))
)

# Iterando sobre os elementos encontrados e imprimindo o texto de cada um
for elemento in elementos:
    print(elemento.text)

driver.quit()
