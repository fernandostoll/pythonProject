preco = float(input('digite o valor da compra'))
print('escolha o codigo de pagamento desejado:'
      '[1] A vista c/ 10% desconto'
      '[2] Cartão 15% desconto'
      '[3] Parcelado 2x s/ juros'
      '[4] parcelado 2x c/ 10%')
opcao = input('opçao:')

if opcao == '1':
    print('valor final:', valor*0.9)
elif opcao == '2':
    print('valor final:', valor*0.85)
elif opcao == '3':
    print('2 parcelas de:', valor/2)
elif opcao == '4':
    print(f'2 parcelas de:,{valor * 1.1 / 2:.2f}')
else:
    print('opção invalida')