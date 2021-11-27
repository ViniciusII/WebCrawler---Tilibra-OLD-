from selenium import webdriver                                
from selenium.webdriver.chrome import service                     
from selenium.webdriver.chrome.service import Service 
from bs4 import BeautifulSoup

#criando a variável para acessar o site da tilibra
url_homepage = 'https://www.tilibraexpress.com.br/'

#Iniciando o service para abrir o arquivo.exe (ChromeDriver) para abrir a página do Chrome 
service = Service('C:/Program Files/Google/Chrome/Application/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

driver.get('url_homepage')

soup = BeautifulSoup(driver.page_source) #Estamos pegando o HTML do que está aberto do Driver

soup.find('img', {'class': 'logo-img'})['src']

#Informações do Produto
url = 'https://www.tilibraexpress.com.br/planner-argolado-17-7-x-24-cm-be-nice-90-g-2022'
driver.get(url)
soup = BeautifulSoup(driver.page_source)
nome = soup.find('h1',{'itemprop': 'name'}).text.strip()
codigo = soup.find('span', {'class': 'product-code'}).text
print(nome)
print(codigo)
