from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


link = str(input('E o link camarada ?:'))


driver = webdriver.Chrome()

driver.get(link)


driver.quit()
