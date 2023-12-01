estoque = 0
movimentacoes = []

while True:
    print('Menu:')
    print('1 - adicionar ao estoque')
    print('2 - retirada do estoque')
    print('3 - consultar saldo')
    print('4 - consultar movimentações')
    print('0 - sair')

    opcao = input('selecione uma opção: ')
    if opcao == '1':
        quantidade = int(input('quantidade a ser adicionada em estoque: '))
        estoque += quantidade


