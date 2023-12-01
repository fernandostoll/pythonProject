anos_pares = 0
anos_impares = 0
anos_bissextos = 0
anos_futuros = 0
anos_passados = 0

while True:
    entrada = input('Digite um ano (ou 0 para sair): ')

    if entrada == '0':
        break

    if entrada:
        ano = int(entrada)

        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            anos_bissextos += 1

        if ano % 2 == 0:
            anos_pares += 1
        else:
            anos_impares += 1

        if 2024 <= ano <= 2025:
            anos_futuros += 1

        if 2000 <= ano <= 2010:
            anos_passados += 1
    else:
        print("Digite um ano válido!")

print(f'Anos pares: {anos_pares}')
print(f'Anos ímpares: {anos_impares}')
print(f'Anos bissextos: {anos_bissextos}')
print(f'Anos futuros (2024, 2025): {anos_futuros}')
print(f'Anos passados (2000, 2010): {anos_passados}')