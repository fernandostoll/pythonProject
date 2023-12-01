candidato_a = open('candidato A.txt', 'r').read().splitlines()
candidato_b = open('candidato B.txt', 'r').read().splitlines()
print(f'total de votos A {len(candidato_a)}')
print(f'total de votos B {len(candidato_b)}')

if len(candidato_a) > len(candidato_b):
    print('Vitoria de A')
elif len(candidato_b) > len(candidato_a):
    print('vitoria de B')
else:
    print('empate')

seta = set(candidato_a)
setb = set(candidato_b)

print(f'Votaram nos 2 candidatos: {len(seta.intersection(setb))}')
set_geral = set_b.union(set_a)
print(f'Não votaram {100-len(set_geral)}')

votos_a = len(set_a.difference(set_b))
votos_b = len(set_b.difference(set_a))

if votos_a == votos_b:
    print('empate')
elif votos_b > votos_a:
    print(f'vitoria B {votos_b}')
else:
    print(f'Vitoria A {votos_a}')

