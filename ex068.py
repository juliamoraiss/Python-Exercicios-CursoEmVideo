from random import randint
print('=-'*30)
print('{:^60}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('=-'*30)
cont = 0
while True:
    n2 = randint(0, 10)
    n = int(input('Diga um valor: '))
    opcao = ' '
    par = (n2 + n) % 2
    total = n + n2
    while opcao not in 'PI':
        opcao = str(input('PAR OU ÍMPAR [P/I]: ')).upper()
    print(f'Você jogou {n} e o computador jogou {n2}. Total {total}.', end = ' ')
    if par == 0:
        print('Deu PAR')
    else:
        print('Deu ÍMPAR.')
    if opcao == 'P':
        if par == 0:
            print('Você VENCEU!')
            print('-'*20)
            cont += 1
        else:
            print('Você PERDEU!')
            print('-' * 20)
            break
    else:
        if par == 0:
            print('Você PERDEU!')
            print('-' * 20)
            break
        else:
            print('Você VENCEU!')
            print('-' * 20)
            cont += 1
print(f'GAME OVER!! Você venceu {cont} vez(es).')
