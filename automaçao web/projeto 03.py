from selenium import webdriver
from time import sleep

navegador = webdriver.Edge()
link = 'https://www.terabyteshop.com.br/perifericos'
navegador.get(link)

sleep(5)
dados = navegador.find_elements('xpath', '//*[contains(concat( " ", @class, " " ), concat( " ", "prod-old-price", " " ))]//span')

for i, preco in enumerate(dados):
    print(i+1, '-', preco.text)