from selenium import webdriver

x = int(input("X: "))
y = int(input("Y: "))
driver = webdriver.Chrome()
link = f"https://dev.prineside.com/en/gtasa_samp_model_id/mapsearch/?x={x}&y={y}"
site = driver.get(link)

print(site)
