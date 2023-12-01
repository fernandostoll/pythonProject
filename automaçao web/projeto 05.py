from selenium import webdriver
from time import sleep

dados = {'nome': 'Fernando',
         'sobrenome': 'Stollmeier',
         'email': 'fernando.stollmeier04@gmail.com',
         'hospedes': '1',
         'mes': 'August',
         'dia': '2',
         'ano': 2023,
         'num_voo': 300,
         'pedidos': 'me busque no aeroporto, preciso chegar rapido no hotel'}


navegador = webdriver.Edge()
navegador.get('https://form.jotform.com/230504787541659')
sleep(6)

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