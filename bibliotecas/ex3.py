#contador de quantidades de digitos
def contar_digitos(numero):
    if numero == 0:
        return 1
    contador = 0
    while numero != 0:
        contador += 1
        numero //= 10
    return contador

numero = 12345
quantidade_digitos = contar_digitos(numero)
print(f'O numero {numero} tem {quantidade_digitos} digitos.')
