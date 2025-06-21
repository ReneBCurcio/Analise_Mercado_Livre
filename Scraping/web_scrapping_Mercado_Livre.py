import requests
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://lista.mercadolivre.com.br/informatica/portateis-acessorios/notebooks/notebook"

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "html.parser")

marca = soup.select('span[class^="poly-component__brand"]')
avaliacao = soup.select('span[class^="andes-visually-hidden"]')
preco = soup.select('span[class^="andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma"]')
## print(i.text.split("Avaliação ")[1].split(" de")[0]) Como extrair o a avaliação
## lista = []
##for i in avaliacao:
##    valor = i.text.split("Avaliação ")[1].split(" de")[0]
##    lista.append(valor)

print(f"Status da requisição: {req.status_code}")
print(f"Marcas encontradas: {len(marca)}")
print(f"Avaliações encontradas: {len(avaliacao)}")
print(f"Preços encontrados: {len(preco)}")
print(soup.prettify()[:2000])