nomes = ['heitor', 'hugo', 'helena']
nomes2 = ['cassio', 'claudete', 'cirilo']
nomes3 = [1, 2, 1.5, False, True, 'carlo']

#nomes.append(nomes2)
#nomes.extend(nomes2)
# nomes += nomes3
# print(nomes)
# nomes.pop()
# print(nomes)
# nomes.remove('helena')
# print(nomes)
# #print(nomes.index('carlos'))
# nomes.pop(nomes.index('carlos'))
# print(nomes)

numeros = [3, 5, 7, 9, 11, 15]
print(numeros.count(3))
print(sum(numeros))

cidades = ['blumenau', 'indaial', 'ascurra', 'pomerode', 'blumenau']
print(cidades.count('ascurra'))

cidades.sort()

print(cidades)
cidades.reverse()
print(cidades)

cidades.insert(0, 'rodeio')
print(cidades)
cidades.clear()
print(cidades)

letras = ['a', 'b', 'c']
palavra = ''
for letra in letras:
    palavra += letra
print(palavra)

alimentos = ['cafe', 'macarrão', 'frango', 'camarão', 'alcatra']

# desempacotamento de lista - list unpacking
bebida, carboidrato, *proteinas, carne = alimentos
print(bebida)
print(carboidrato)
print(proteinas)
print(carne)

negativos = [-3, -8, -15, -35, -16, -4]
positivos = [-1 * valor for valor in negativos]
print(positivos)

pares = [valor for valor in positivos if valor %2==0]
print(pares)
