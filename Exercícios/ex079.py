valores = []
opcao = 'S'
while opcao == 'S':
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado não adicionado.')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-'*30)
valores.sort()
print(f'Você digitou os valores: {valores}')