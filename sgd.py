from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('file:///home/Joe/%3C!DOCTYPE%20html%3E.html')

time.sleep(5)


try:
    # Localize o elemento que contém o texto "Ativo:" e obtenha seu texto
    elemento_ativo = browser.find_element(
        By.XPATH, '//td[contains(text(), "Ativo:")]/following-sibling::td')
    texto_ativo = elemento_ativo.text.strip()
    print("Ativo:", texto_ativo)

    # Localize o elemento que contém o texto "Contrato ativo:" e obtenha seu texto
    elemento_contrato = browser.find_element(
        By.XPATH, '//td[contains(text(), "Contrato ativo:")]/following-sibling::td')
    texto_contrato = elemento_contrato.text.strip()
    print("Contrato ativo:", texto_contrato)

except Exception as e:
    print("Erro ao localizar elemento:", e)


time.sleep(60)
