print('-' * 30)
print('{:^30}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
n0 = 0
n1 = 1
n2 = n0 + n1
print('{} -> {} -> {}'.format(n0, n1, n2), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1

