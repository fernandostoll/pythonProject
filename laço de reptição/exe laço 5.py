print('CADASTRO DE PRODUTOS!')
print('Quantos produtos voce deseja cadastrar?')
qtd = int(input('resposta: '))

print('======================')

produtos = []
precos = []
for i in range(1, qtd+1):
    produtos = input(f'produtos{i}: ')
    preco = input(f'preço: R$ ')
    produtos.append(produtos)
    precos.append(preco)

print('====================')

for i in range(qtd):
    print(f'produto: {produtos[i]} - preço: R$ {precos[i]}')