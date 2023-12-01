def verifica_palindromo(palavra):
    palavra = palavra.replace('', '').lower()
    
    return palavra == palavra[::-1]

palavra = 'MUSUM'
if verifica_palindromo(palavra):
    print(f'{palavra} é um palindromo')
else:
    print(f'{palavra} não é um palindromo')
