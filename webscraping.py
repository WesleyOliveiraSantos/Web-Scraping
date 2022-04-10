import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
page = requests.get("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome..69i57j0i131i433i512l5j0i433i512j0i3j0i131i433i512l2.1049j1j15&sourceid=chrome&ie=UTF-8",headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

atributos = {'class':'g'}

valor_dolar = soup.find_all("span",class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])