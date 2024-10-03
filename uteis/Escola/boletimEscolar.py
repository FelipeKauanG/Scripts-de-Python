from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

materiaClass = "tALeft"

link = str(input('E o link camarada ?:'))


driver = webdriver.Chrome()

driver.get(link)


elementos = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, materiaClass)))



print(f"\n\033[94mMatérias\033[m\n")

for i in range(1, 14):
    print(elementos[i]. text)

driver.quit()
