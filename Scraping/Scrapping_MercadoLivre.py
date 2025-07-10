import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import random

url = "https://lista.mercadolivre.com.br/informatica/portateis-acessorios/notebooks/notebook"

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

edge_options = Options()
edge_options.add_argument('--no-sandbox') ## Para evitar possíveis erros de segurança em servidores Linux/Produção
edge_options.add_argument('--disable-dev-shm-usage') ## evita compartilhamento da memória de disco e a RAM, visando otimizar o processo
edge_options.add_argument('--disable-blink-features=AutomationControlled') ## Argumento utilizado para evitar os bloqueos via bot do sistema 
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"]) ## Argumento utilizado para evitar os bloqueos via bot do sistema 
edge_options.add_experimental_option('useAutomationExtension', False) ## Argumento utilizado para evitar os bloqueos via bot do sistema 

driver = None  # Define antes do try

try:
    driver = webdriver.Edge(options=edge_options)
    driver.get(url)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "poly-card__content"))
    )
    time.sleep(random.uniform(2, 4))
    
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    
except WebDriverException as e:
    print(f"Erro de WebDriver: {e}")
except Exception as e:
    print(f"Erro geral: {e}")
finally:
    if driver:
        try:
            driver.quit()
            print("Driver fechado com sucesso")
        except:
            print("Erro ao fechar driver")

try:
    Nota = soup.find_all("span", class_="poly-reviews__rating")
    if not Nota:
        print("Nenhuma nota encontrada")
except Exception as e:
    print(f"Erro na extração da parte de notas, erro: {e}")


try:
    Avalicoes = soup.find_all("span", class_="poly-reviews__total")
    if not Avalicoes:
        print("Nenhuma avaliação encontrada")
except Exception as e:
    print(f"Erro na extração da parte de avaliações, erro: {e}")

try:
    Preco = soup.find_all("span", class_="andes-money-amount andes-money-amount--cents-superscript")
    if not Preco:
        print("Nenhum preço encontrado")
except Exception as e:
    print(f"Erro na extração da parte de preço, erro: {e}")

try:
    Vendedor = soup.find_all("span", class_="poly-component__seller")
    if not Vendedor:
        print("Nenhum vendedor encontrado")
except Exception as e:
    print(f"Erro na extração da parte de vendedor, erro: {e}")

try: 
    Item = soup.find_all("span", class_="poly-component__title")
    if not Item:
        print("Nenhum item encontrado")
except Exception as e:
    print(f"Erro na extração da parte de item, erro: {e}")
