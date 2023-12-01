from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

dados = {'nome': 'Fernando Stollmeier',
         'data_nacimento': '05-08-2004',
         'email': 'fernando.stollmeier04@gmail.com'}

navegador = webdriver.Edge()
navegador.get('https://form.jotform.com/221878303914661')
sleep(2)

# preencher formulario
navegador.find_element('id', 'input_42').send_keys(dados['nome'])
navegador.find_element('id', 'lite_mode_7').send_keys(dados['data_nacimento'])
navegador.find_element('id', 'input_5').send_keys(dados['email'])

# enviar formulario
navegador.find_element('id', 'input_40').click()


input()