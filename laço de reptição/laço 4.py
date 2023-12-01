numero = 17

for i in range(2, numero):
    if numero % i == 0:
        print('não é primo')
        break
else:
    print('é primo')
