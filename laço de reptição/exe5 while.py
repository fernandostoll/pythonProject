conta = 'abc123'
senha = 'senac'

conta_digitada = input('Qual conta:')
senha_digitada = input('Qual senha:')

if conta == conta_digitada and senha_digitada == senha:
    saldo = 1000
    movimentacoes = []

    while True:
        print('[1] Consultar saldo')
        print('[2] Pagar conta')
        print('[3] Depositar')
        print('[4] Sacar')
        print('[5] Sair')
        print('[6] Extrato')
        opcao = input('Qual opção:')

        if opcao == '1':
            print(f'Saldo: {saldo}')

        elif opcao == '2':
            descricao = input('Qual a conta:')
            valor = float(input('Qual o valor:'))

            if 0 < valor >= saldo:
                print('Não há saldo suficente')
            else:
                saldo -= valor
                movimentacoes.append(f'Descrição: {descricao} - R$ {valor}')
                print(f'Saldo Atualizado: {saldo}')

        elif opcao == '3':
            valor = float(input('Qual o valor:'))
            if valor < 0:
                print('Caloteiro')
            else:
                saldo += valor
                movimentacoes.append(f'Descrição: Depósito - R$ {valor}')
                print(f'Saldo Atualizado: {saldo}')

        elif opcao == '4':
            valor = float(input('Qual o valor:'))
            if 0 < valor >= saldo:
                print('Não há saldo suficente')
            else:
                saldo -= valor
                movimentacoes.append(f'Descrição: Saque - R$ {valor}')
                print(f'Saldo Atualizado: {saldo}')

        elif opcao == '5':
            break
        elif opcao == '6':
            for movimento in movimentacoes:
                print(movimento)
            print('Saldo final:', saldo)
        else:
            print('Opção Inválida')
else:
    print('Conta ou senha incorretos')