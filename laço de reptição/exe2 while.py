numero = int(input('digite um numero positivo inteiro:'))
fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f'O fatorial do {numero} é {fatorial}')