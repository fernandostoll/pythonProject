lista_antigo = open('clientes sistema antigo.txt', 'r').read().splitlines()
lista_novo = open('clientes sistema novo.txt', 'r').read().splitlines()

lista_total = lista_novo + lista_antigo
set_total = set(lista_total)
set_duplicados = set()

for cnpj in lista_total:
    if lista_total.count(cnpj)>1:
        set_duplicados.add(cnpj)
        cont += 1

print(f'intens duplicados: {len(set_duplicados)}')
print(f'total de cadastros {len(lista_total)}')
print(f'repeditos removidos: {len(lista_total)}')
print(f'itens a remover para não ter duplicados {cont - len(set_total)}')





