def calcule_media(lista):
    if len(lista) == 0:
        return None

    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 25, 7, 42, 8, 56]
media = calcule_media(numeros)
print(f'A media dos numeros na lista é: {media}')