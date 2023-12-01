#suposto linha de cnpjs
cnpjs = [
    '12345678901234',
    '98765432109876',
    '12345678901234',
    '55555555555555',
    '98765432109876'
]

cnpj_set = set()

cnpj_duplicados = set()

for cnpj in cnpjs:
    if cnpj in cnpj_set:
        cnpj_duplicados.add(cnpj)
    else:
        cnpj_set.add(cnpj)

print('CNPJs duplicados:', cnpj_duplicados)