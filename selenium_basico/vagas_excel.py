from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.vagas.com.br/vagas-de-ti-em-sao-paulo")
time.sleep(6)

vagas = driver.find_elements(By.CLASS_NAME, "vaga")
print(f"Vagas encontradas na página: {len(vagas)}")

lista = []

data_coleta = datetime.now().strftime("%d-%m-%Y")

for vaga in vagas:
    try:
        titulo = vaga.find_element(By.CLASS_NAME, "cargo").text
        empresa = vaga.find_element(By.CLASS_NAME, "emprVaga").text
        local = vaga.find_element(By.CLASS_NAME, "vaga-local").text
        link = vaga.find_element(By.TAG_NAME, "a").get_attribute("href")

        if "SP" in local or "São Paulo" in local or "Guarulhos" in local:
            lista.append({
                "Título da Vaga": titulo,
                "Empresa": empresa,
                "Local": local,
                "Link": link,
                "Data da Coleta": data_coleta
            })
    except:
        pass

driver.quit()

df = pd.DataFrame(lista)

nome_arquivo = f"vagas_ti_sp_{data_coleta}.xlsx"
df.to_excel(nome_arquivo, index=False)

print(f"✅ {len(df)} vagas salvas no arquivo {nome_arquivo}")

