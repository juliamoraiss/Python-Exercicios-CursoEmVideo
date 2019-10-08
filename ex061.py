print('=' * 41)
print('{:^41}'.format('10 PRIMEIROS TERMOS DE UMA PA'))
print('=' * 41)
a1 = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão? '))
soma = a1
cont = 0
while cont <= 9:
    print(soma, end=' ')
    soma += r
    cont += 1
print('FIM')