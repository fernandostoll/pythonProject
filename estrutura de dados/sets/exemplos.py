lista = list(range(5, 11))
lista2 = list(range(3))

set1 = set(lista+lista2)
print(set1)
print(type(set1))

#adicionar itens ao set
set1.add(15)
print(set1)

lista3 = [22,65,18,92]
set1.update(lista3)
print(set1)

#remove e discard para apagar elementos de um set
#caso não encontrado, o discard ignora, e o remove retorna keyerror
set1.remove(92)
print(set1)

set1.pop()
print(set1)

set1.clear()
print(set1)
