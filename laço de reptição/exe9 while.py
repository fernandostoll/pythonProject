while True:
    print('menu:')
    print('1 - opção 1')
    print('0 - sair')

    opcao = input('selecione um opção: ')

    if opcao == '1':
        print('voce selecionou a opção 1')
    elif opcao == '0':
        print('saindo do programa...')
        break
    else:
        print('opção invalida. selecione 1 ou 0.')
