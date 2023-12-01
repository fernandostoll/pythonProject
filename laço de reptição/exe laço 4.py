print('TABUADAS!')

while True:
    numero = int(input('digite um numero para ver sua tabuada (ou digite 0 para sair):'))
    if numero == 0:
        print('encerrando o programa.')
        break

    print('tabuada do', numero)
    for i in range(1, 11):
        resultado = numero * i
        print(numero, 'x', i, '=', resultado)

