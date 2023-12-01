cnpj = input('Digite seu CNPJ: ')
#123.214/14324-1
simbolos = ".-//"
verificacao = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
result_multi = []
codigos = list(cnpj)
soma1 = 0

#tirando simbolos das variaveis
for i in range(len(codigos)):
    if i > len(simbolos[i]):
        break
    cnpj = cnpj.replace(simbolos[i], '')
cnpj = cnpj.replace('/', '')


if len(cnpj) != 14:
    print('cnjp invalido1')

#verificar se os digitos sao iguais
if cnpj == cnpj[0] * 14:
    print('cnpj invalido')


#Multiplicando todos os numeros e somando os resultados
for i in range(len(codigos) - 2):
    multiplicacao = int(codigos[i]) * int(verificacao[i])
    result_multi.append(multiplicacao)

for i in range(len(result_multi)):
    soma1 += int(result_multi[i])


#aplicando a formula de verificação
pre_verificacao = 11 - soma1 % 11
if pre_verificacao == 0 or pre_verificacao == 1:
    verificacao1 = 0

