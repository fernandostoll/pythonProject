def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


def saudar():
    return 'bom dia!'


def get_perimeter(base, altura):
    return 2 * (base+altura)


def is_square(base: int, altura: int):
    if base == altura:
        return True
    return False


def saudar_manha(nome):
    return f'bom dia {nome}'


def istriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
lado1 = 8
lado2 = 4
lado3 = 6

if istriangle(lado1, lado2, lado3):
    print('é um triangulo')
else:
    print('não é um triangulo')


def verificar_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        return True
    else:
        return False

ano = int(input('digite um ano: '))
if verificar_ano_bissexto(ano)
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é bissexto.')