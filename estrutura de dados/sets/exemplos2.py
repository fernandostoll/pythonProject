set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9, 22}

#unir 2 sets
print(f'union {set2.union(set1)}')

#interseção
print(f'intersection {set2.intersection(set1)}')

#diferenças
print(f'difference {set2.difference(set1)}')
print(f'difference {set1.difference(set2)}')
print(f'symmetric Difference {set1.symmetric_difference(set2)}')

if 22 in set2:
    print('achou!')