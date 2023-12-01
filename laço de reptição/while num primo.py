# 7
#
# 7%2 !=0
# 7%3 !=0
# 7%4 !=0
# 7%5 !=0
# 7%6 !=0
#
# for i in range(2,7):

# programa que so para quando o numero for primo
while True:
    numero = int(input('Digite um numero:'))
    if numero < 2:
        print('Não é primo')
    else:
        for i in range(2, numero//2+1):
            if numero % i == 0:
                print('Não é primo')
                break
        else:
            print('É primo')
            break