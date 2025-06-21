import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://lista.mercadolivre.com.br/informatica/portateis-acessorios/notebooks/notebook"


req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

marca = soup.select('span[class^="poly-component__brand"]')
avaliacao = soup.select('span[class^="andes-visually-hidden"]')
preco = soup.select('span[class^="andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma"]')
## print(i.text.split("Avaliação ")[1].split(" de")[0]) Como extrair o a avaliação
## lista = []
##for i in avaliacao:
##    valor = i.text.split("Avaliação ")[1].split(" de")[0]
##    lista.append(valor)

j = 0
for i in marca:
    j = j + 1

j_1 = 0
for i in avaliacao:
    j_1 = j_1 + 1

j_2 = 0
for i in preco:
   j_2 = j_2 + 1 

print(j)
print(j_1)
print(j_2)