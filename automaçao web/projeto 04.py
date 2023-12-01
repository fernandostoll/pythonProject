from selenium import webdriver
from time import sleep

navegador = webdriver.Edge()
link = 'https://g1.globo.com/mundo/ao-vivo/guerra-hamas-israel.ghtml'
navegador.get(link)

sleep(2)
dados = navegador.find_element('titulo', 'data')

print()
