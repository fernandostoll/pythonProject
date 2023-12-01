dicionario = {'chave 1': 'jonas',
              'chave 2': 'adriana',
              'chave 3': 'ariadne'
              }
# print(dicionario['chave 3'])

emails = {'jonas': 'jonasreiter@hotmail.com',
          'delva': 'delva_das_quebradas@gmail.com',
          'juvenal': 'canetaazul@ual.com.br',
          'nestor': 'nenenestor@bol.com.br'}


print(emails['nestor'])
print(emails.get('arthur', 'Não existente'))

#adicionar itens ao dicionario
emails['tristan'] = 'tristinho@gmail.com'
print(emails.get('tristan', 'não existe'))

#alterar valor do dicionario
emails['tristan'] = 'tristinho@bol.com'
emails.update({'jonas': 'jonas.reiter92@gmail.com'})
print(emails)

#alterar nome da chave
emails['jonasreiter'] = emails.pop('jonas')
print(emails)

#alterar nome da chave metodo 2
emails['jonas'] = emails['jonasreiter']
del emails['jonasreiter']
print(emails)

#imprimir todas as chaves
print(emails.keys())

#imprimir todos os valores
print(emails.values())

#percorrer todos as chave do dicionario
for chave in emails:
    print(chave)

#percorrer todos os valores do dicionario
for valor in emails:
    print(emails[valor])

#percorrer dicionario completo
for chave, valor in emails.items():
    print(f'{chave} --------{valor}')

#deletar um chave
emails.pop('tristan')
print(emails)

#deletar ultima chave
emails.popitem()
print(emails)

#verificar se uma chave existe
if 'joaquim' in emails:
    print('existe')
else:
    print('não existe')

if 'canetaazul@oul.com.br' in emails.values():
    print('existe')
else:
    print('não existe')

emails2 = {'carlos': 'carlos@gmail.com',
           'sandra': 'sandrina@gmail.com'
           }
emails_geral = {**emails, **emails2}
print(emails_geral)

#transformar 2 listas em dicionario
lista_nomes = ['jonas', 'marcela', 'aristides', 'gilberta']
notas = [7, 8, 9, 10]

#metodo bruto
dicionario_novo = dict()
for i in range(len(lista_nomes)):
    dicionario_novo[lista_nomes[i]] = notas[i]
print(dicionario_novo)

#metodo nutella
dicionario_novo2 = dict(zip(lista_nomes, notas))
print(dicionario_novo2)