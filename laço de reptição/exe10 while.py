senha_correta = ('1234')
tentativas = 3

while tentativas > 0:
    senha = input('Digite a senha de quatro numeros: ')
    if senha == senha_correta:
        print('Senha correta')
        break
    else:
        tentativas -= 1
        print(f'Senha incorreta. Você tem {tentativas} tentativas')
    if tentativas == 0:
        print('Tentativas esgotadas. Acesso bloqueado.')