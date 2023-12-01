def encontrar_palavra_mais_longa(lista_palavras):
    if not lista_palavras:
        return None

    palavra_mais_longa = ''

    for palavra in lista_palavras:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra
    return palavra_mais_longa

palavras = ['gato', 'cachorro', 'elefante', 'papagaio', 'hipopotamo']
mais_longa = encontrar_palavra_mais_longa(palavras)
print(f'A palavra mais longa na lista é: {mais_longa}')
