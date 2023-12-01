cotacao = [4.99, 5.43, 6.35, 1]

print('qual moeda voce deseja?'
      '[1] dolar'
      '[2] euro'
      '[3] libra esterlina'
      '[4] real')
moeda_desejada = int(input('qual opção:'))

print('qual moeda voce tem?'
      '[1] dolar'
      '[2] euro'
      '[3] libra esterlina'
      '[4] real')
moeda_atual = int(input('qual opção:'))

valor = float(input('quanto voce possui?'))

print('conversão:', valor*cotacao[moeda_atual-1]/cotacao[moeda_desejada-1])

