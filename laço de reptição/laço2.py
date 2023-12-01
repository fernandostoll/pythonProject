maior_valor = 0
for i in range(5):
    numero = float(input('numero:'))

    if numero > maior_valor:
        maior_valor = numero

print('maior valor informado:', maior_valor)