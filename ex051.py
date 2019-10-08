print('=' * 41)
print('{:^41}'.format('10 PRIMEIROS TERMOS DE UMA PA'))
print('=' * 41)
a1 = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão? '))
a10 = a1 + ((11 - 1) * r)
for c in range(a1, a10, r):
    print(c, end=" -> ")
print('FIM')
