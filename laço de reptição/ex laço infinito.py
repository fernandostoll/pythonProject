numeros = []

while True:
    entrada = input('digite um numero (ou digite qualquer letra para encerrar): ')
    if entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit()):
        numero = float(entrada)
        numeros.append(numero)
    else:
        break

numeros_ordenados_crecentes = []
numeros_ordenados_decrecente = []
soma = 0

for num in numeros:
    index = 0
    while index < len(numeros_ordenados_crecentes) and num > numeros_ordenados_crecentes[index]:
        index += 1
        