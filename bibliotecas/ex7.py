def encontrar_maior_valor(lista):
    if len(lista) == 0:
        return None

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

numeros = [10, 25, 7, 42, 8, 56]
maior_valor = encontrar_maior_valor(numeros)
print(f'O maior valor na lista é: {maior_valor}')
