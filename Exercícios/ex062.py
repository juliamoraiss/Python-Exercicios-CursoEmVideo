print('=' * 41)
print('{:^41}'.format('10 PRIMEIROS TERMOS DE UMA PA'))
print('=' * 41)
a1 = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão? '))
soma = a1
cont = 1
opcao = 10
total = 0
while opcao != 0:
    total += opcao
    while cont <= total:
        print(soma, end=' ')
        soma += r
        cont += 1
    print('PAUSA')
    opcao = int(input('Quantos termos mais você deseja ver? '))
print('Progressão finalizada com {} termos'.format(total))

