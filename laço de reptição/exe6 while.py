intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

numero = float(input('informe um numero (negativo para encerrar):'))

while numero >= 0:
    if numero >= 0 and numero <= 25:
        intervalo_0_25 += 1
    elif numero <= 50:
        intervalo_26_50 += 1
    elif numero <= 75:
        intervalo_51_75 += 1
    elif numero <= 50:
        intervalo_76_100 += 1

    numero = float(input('informe um numero (negativo para encerrar):'))

print(f'numeros no intervalo [0-25]: {intervalo_0_25}')
print(f'numeros no intervalo [26-50]: {intervalo_26_50}')
print(f'numeros no intervalo [51-75]: {intervalo_51_75}')
print(f'numeros no intervalo [76-100]: {intervalo_76_100}')