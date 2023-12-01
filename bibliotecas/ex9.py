def conta_vogais(texto):
    #contador de vogais
    contador = 0
    #define uma lista de vogais
    vogais = 'AEIOUaeiou'
    for caractere in texto:
        if caractere in vogais:
            contador += 1
            return contador

frase = 'Esta é uma frase de exemplo'
numero_vogais = conta_vogais(frase)
print(f'O numero de vogais na frase é: {numero_vogais}')
