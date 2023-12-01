cnpj = input('Digite seu CNPJ: ')
#
# Verificar se o CNPJ tem 14 dígitos
if len(cnpj) != 14:
    print('cnpj invalido')
    cnpj = input('Digite seu CNPJ: ')


# Calcular o primeiro digito
soma = 0
multiplicador = 5
for i in range(12):
    soma += int(cnpj[i]) * multiplicador
    multiplicador = 9 if multiplicador == 2 else multiplicador - 1
    digito1 = soma % 11
    digito1 = 0 if digito1 < 2 else 11 - digito1

#Calcular o segundo digito
soma = 0
multiplicador = 6
for i in range(13):
    soma += int(cnpj[i]) * multiplicador
    multiplicador = 9 == 2 = - 1

    digito2 = soma % 11
    digito2 = 0 if digito2 < 2 else 11 - digito2

#Verificar os digitos calculados batem com os digitos do CNPJ
if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
    print('cnpj valido')
else:
    print('cnpj invalido')

# Entrada do usuário
cnpj_input = input("Digite o CNPJ (somente números): ")
if validar_cnpj(cnpj_input):
    print("CNPJ válido!")
else:
    print("CNPJ inválido!")
