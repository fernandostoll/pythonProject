from selenium import webdriver
from time import sleep

#PARTE 1
navegador = webdriver.Edge()
navegador.get('https://externo.proway.com.br/login-aluno')
sleep(7)

# preencher formulario
navegador.find_element('id', 'first_105').send_keys(dados['nome'])
navegador.find_element('id', 'last_105').send_keys(dados['sobrenome'])
navegador.find_element('id', 'input_17').send_keys(dados['email'])
navegador.find_element('id', 'input_18').send_keys(dados['hospedes'])
navegador.find_element('id', 'input_20_day').send_keys(dados['dia'])
navegador.find_element('id', 'input_20_month').send_keys(dados['mes'])
navegador.find_element('id', 'input_20_year').send_keys(dados['ano'])
navegador.find_element('id', 'label_input_10_0').click()
navegador.find_element('id', 'input_28').send_keys(dados['num_voo'])
navegador.find_element('id', 'input_30').send_keys(dados['pedidos'])


#enviar formulario
navegador.find_element('id', 'input_2').click()

input()