import requests
from bs4 import BeautifulSoup
import wget

url = "https://datasets.imdbws.com/"
#url = "https://portaldatransparencia.gov.br/download-de-dados/licitacoes"
link_list = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

for a in soup.find_all("a", href = True):
    link_list.append(a["href"])
    print(f'{a}\n')

i = 0
for link in link_list:
    i = i + 1
    print(f"Downloading File {i}...")
    wget.download(link)
    
print("All Downloads Finished")