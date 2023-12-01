def verificador_par_ou_impar():
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        return 'par'
    return 'impar'

resultado = verificador_par_ou_impar()
print(f'O numero é {resultado}')