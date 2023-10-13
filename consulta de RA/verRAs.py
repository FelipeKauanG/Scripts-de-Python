try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import numpy as np
    
    # Dados do aluno
    ra = int(input("Insira aqui seu RA: "))
    data = str(input("Sua data de nascimentos '01/02/1234: '"))
    digito = int(input("Seu dígito: "))

    # configurando o Driver
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
                
                    
                for notn in range(1, 13): # localiza as matérias
                    for bim in range(2, 15, 4): # localiza os bimestres
                        disciplinas = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[1]")))[0].text
                        bimnot = wait.until(EC.presence_of_all_elements_located(
                            (By.XPATH, f'/html/body/div/div/div[4]/table/tbody/tr[{notn}]/td[{bim}]')))[0].text
                        cleaned_bimnot = str(bimnot).replace(" ", "").replace("-","")
                        if cleaned_bimnot.isdigit():
                            pontos += int(bimnot)
                            num.append(bimnot)
                    #print()
            except Exception:
                print("\n\n\n")
        except Exception:
            print(f"Não consegui ver este boletim!")
    driver.quit()
    num = np.array(num).reshape(len(num/4),4)
    print(f"Pontos totais: {pontos}\nMédia total do aluno: \033[36m{pontos / len(num):.2f}\033[m")
    print(num)
except:
    print("bom dia")
    