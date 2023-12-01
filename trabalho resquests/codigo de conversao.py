import requests

# Chave de API (substitua pela sua própria chave)
api_key = "SUA_CHAVE_DE_API_AQUI"

# URL base da API
base_url = "https://open.er-api.com/v6/latest/"

real = float(input('Quanto dinheiro você tem: '))
dolar = real / 3.27
print('Com R${:.2f} você pode converter em US${:.2f}'.format(real, dolar))

# Dicionário para a taxa de câmbio
taxas_de_cambio = {}

#Fazer a solicitação GET para a API
url = f'{base_url}/BRL'  # Assuming you want to convert from BRL to USD

#Parametros de solicitação GET
params = {
    "apikey": api_key,
    "symbols": "USD"
}

#Fazer a solicitação GET para a API
response = requests.get(url, params=params)

#Verificar a solicitação
if response.status_code == 200:
    data = response.json()
    taxas_de_cambio["BRL"] = {"USD": data["rates"]["USD"]}
else:
    print(f"Falha na solicitação da API para USD")

#taxas de câmbio
for moeda_origem, taxas in taxas_de_cambio.items():
    print(f'Taxas de câmbio para 1 {moeda_origem}:')
    for moeda_destino, taxa in taxas.items():
        print(f'{moeda_destino}: {taxa}')

