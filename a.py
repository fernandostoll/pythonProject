cpf = input('Digite seu cpf: ')

while True:
    if len(cpf) != 11:
        print('cpf invalido1')
        cpf = input('Digite seu cpf: ')

    if cpf == cpf[0] * 11:
        print('false')