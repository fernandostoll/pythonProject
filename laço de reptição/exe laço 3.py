mulheres = []
homens = []

print('DUPLAS!')
for i in range(3):
    nome = input(f'mulher {i+1}: ')
    mulheres.append(nome)

print(f'mulheres: {mulheres}')

for i in range(3):
    nome = input(f'homem {i+1}: ')
    homens.append(nome)

print(f'homens: {homens}')

for i in range(3):
    print(f'dupla: {homens[i]} e {mulheres[i]}')