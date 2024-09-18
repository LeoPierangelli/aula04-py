'''senha = input('Digite a senha: ')

if senha == '1234':
    print('Acesso permitido')
else:
    print('Acesso negado')
    while senha != '1234':
        senha = input('Digite a senha novamente: ')
        if senha == '1234':
            print('Acesso permitido')
        else:
            print('Acesso negado')'''

senha_cadastrada = '1234'
senha = input('Diga sua senha: ')
while senha != senha_cadastrada:
    senha = input('Digite a senha novamente: ')
print('Acesso permitido:')


