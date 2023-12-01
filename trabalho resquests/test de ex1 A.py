#Mude os valores e gere uma imagem de cachorro com o API shibe.online. Imprima um novo URL.
import requests

# definiçao de parametros de solici
url = "http://shibe.online/api/shibes"
params = {
    "count": 1,  # Quantidade de imagens de cachorro
    "urls": True  # Para pegar URL diretos das imagens
}

#solicitação da api
reponse = requests.get(url,params=params)

#verificaçao sucedida
if reponse.status_code == 200:
    data = reponse.json()
    if data:
        image_url = data[0] #url da imagem
        print('url da imagem do cachorro:', image_url)
    else:
        print('nenhuma imagem de cachorro encontrada na resposta da API.')
else:
    print('Erro ao fazer a solicitação a API shibe.online:', reponse.status_code)

