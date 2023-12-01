#converção de moeda
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)
print(requisicao.json())
#
#
# #cep
import requests

requisicao = requests.get('https://cep.awesomeapi.com.br/json/05424020')
print(requisicao)
print(requisicao.json())

# localizador de ip
import requests

requisicao = requests.get('https://api.invertexto.com/v1/geoip/200.33.152.248?token=SEUTOKEN')
print(requisicao)
print(requisicao.json())