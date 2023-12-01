#61.290.461/0001-30
cnpj = input('Digite seu CNPJ: ')
123.214/14324-1
simbolos = ".-//"
verificacao = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
result_multi = []
result_multi2 = []
codigos = list(cnpj)
soma1 = 0
verificacao2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

#tirando simbolos das variaveis
for i in range(len(codigos)):
    if i > len(simbolos[i]):
        break
    cnpj = cnpj.replace(simbolos[i], '')
cnpj = cnpj.replace('/', '')

#Condição de existencia
while True:
    if len(cnpj) != 14:
        print('CNPJ invalido1')
        cnpj = input('Digite seu CNPJ: ')

        for i in range(len(codigos)):
            if i > len(simbolos[i]):
                break
            cnpj = cnpj.replace(simbolos[i], '')
        cnpj = cnpj.replace('/', '')

    else:
        break

while True:
    if cnpj == cnpj[0] * 14:
        print('CNPJ invalido')
        cnpj = input('Digite seu CNPJ: ')

        for i in range(len(codigos)):
            if i > len(simbolos[i]):
                break
            cnpj = cnpj.replace(simbolos[i], '')
        cnpj = cnpj.replace('/', '')

    else:
        break

#Multiplicando todos os numeros e somando os resultados
for i in range(len(cnpj) - 2):
    multiplicacao = int(cnpj[i]) * int(verificacao[i])
    result_multi.append(multiplicacao)

for i in range(len(result_multi)):
    soma1 += int(result_multi[i])

# #aplicando a formula de verificação
pre_verificacao = soma1 // 11
resto = soma1 - (11*pre_verificacao)
dig1 = 0
soma2 = 0

if resto == 0 or resto == 1:
    dig1 = 0
else:
    dig1 = 11 - resto

#Multiplicando todos os numeros e somando os resultados 2
for i in range(len(cnpj) - 1):
    multiplicacao2 = int(cnpj[i]) * int(verificacao2[i])
    result_multi2.append(multiplicacao2)

for i in range(len(result_multi2)):
    soma2 += int(result_multi2[i])

# #aplicando a formula de verificação2
pre_verificacao2 = soma2 // 11
resto2 = soma2 - (11*pre_verificacao2)
dig2 = 0
soma2 = 0

if resto2 == 0 or resto2 == 1:
    dig2 = 0
else:
    dig2 = 11 - resto2

if dig1 == int(cnpj[12]) and dig2 == int(cnpj[13]):
    print('CNPJ valido!')
else:
    print('CNPJ invalido!')