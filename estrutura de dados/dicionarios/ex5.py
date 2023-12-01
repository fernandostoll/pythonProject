#criar arquivo
with open('nomes.txt', 'w') as nomes_file:
    nomes_file.write('Fernando\nBob\nwesley\nDavid\nrafael')

#cria email
with open('emails.txt', 'w') as emails_file:

    emails_file.write("fernando@example.com\nbob@example.com\nwesley@example.com\ndavid@example.com\nrafael@example.com")

#dicionario vazio para add dados
dados = {}

#le arquivos email
with open('nomes.txt', 'r') as nomes_file:
    nomes = nomes_file.read().splitlines()

# Ler e-mails do arquivo e-mails
with open('emails.txt', 'r') as emails_file:
    emails = emails_file.read().splitlines()

#verificado dde numeros e nomes e email
if len(nomes) == len(emails):
    #dicionario para cobinar nomes e email
    dados = dict(zip(nomes, emails))
    #ordenar por chave
    dados_ordenados = dict(sorted(dados.items()))

    #exibir dicionario
    print('dicionario ordenado por nomes: ')
    for nome, email in dados_ordenados.items():
        print(f'Nome: {nome}, E-mail: {email}')
else:
    print('O numero de nomes e e-mails não corresponde')