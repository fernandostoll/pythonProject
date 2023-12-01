# Escolha um API qualquer e personalize as impressões das mensagens de status mais comuns: 200, 404 e 500.
import requests

def get_data_from_api(endpoint):
    url = f'https://jsonplaceholder.typicode.com/{endpoint}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Solicitação bem sucedida! dados obtidos:')
            print(response.json())
        elif response.status_code == 404:
            print('Erro 404: recurso não encontrado.')
        elif response.status_code == 500:
            print('Erro 500: Erro interno do servidor.')
        else:
            print(f'status code inesperado: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Erro de conexão: {e}')

# Exemplos de uso
print("Exemplo 1 - Status 200:")
get_data_from_api("posts/1")

print("\nExemplo 2 - Status 404:")
get_data_from_api("posts/1000")

print("\nExemplo 3 - Status 500:")
get_data_from_api("posts/0")