def contar_letra(string, letra):
    contador = 0
    for char in string:
        if char == letra:
            contador += 1
    return contador

#exemplo de uso:
texto = 'Esta é uma amostra de texto com algumas letras.'
letra_alvo = 'a'
resultado = contar_letra(texto, letra_alvo)
print(f"A letra '{letra_alvo}' aparece {resultado} vezes na string. ")

