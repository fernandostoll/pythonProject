contador = 0
soma = 0
positivos = 0
negativos = 0
valor_maximo = float('-inf')
valor_minimo = float('inf')

while True:
    valor = float(input('Digite um valor (ou digite 0 para sair): '))

    if valor == 0:
        break

    soma += valor
    contador += 1

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

    if valor > valor_maximo:
        valor_maximo = valor
    if valor < valor_minimo:
        valor_minimo = valor

if contador == 0:
    print('Nenhum valor foi inserido.')
else:
    media = soma / contador
    percentual_positivos = (positivos / contador) * 100
    percentual_negativos = (negativos / contador) * 100

    print(f'Média aritmética: {media:.2f}')
    print(f'Quantidade de valores positivos: {positivos}')
    print(f'Quantidade de valores negativos: {negativos}')
    print(f'Percentual de valores positivos: {percentual_positivos:.2f}%')
    print(f'Percentual de valores negativos: {percentual_negativos:.2f}%')
    print(f'Valor máximo: {valor_maximo}')
    print(f'Valor mínimo: {valor_minimo}')