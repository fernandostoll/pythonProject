# #laço de reptição é um estrutura que roda mais de uma vez
#  FOR - para
#  while - enquanto
#
#  for i in range(10): #0,1,2,3,4,5,6,7,8,9 (roda 10 vezes)
#     print(i)

# for i in range(5):
#     print('Fernando')

# for i in 'Fernando':
#     print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f'{i} - par')
#     else:
#         print(f'{i} - impar')

nome = 'arazra'
letra = 'a'
letra_saida = 'z'

total = 0
for i in nome:
   if i == letra:
       total += 1
   if i == letra_saida:
           break
print(total)

