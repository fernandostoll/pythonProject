def inverter_numero(numero):
    numero_str = str(numero)

    numero_invertido_str = numero_str[::-1]

    numero_invertido = int(numero_invertido_str)

    return  numero_invertido

numero_original = 127
numero_invertido = inverter_numero(numero_original)
print(f'O numero original {numero_original} invertido é {numero_invertido}')