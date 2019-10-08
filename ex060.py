n = int(input('Digite um número para calcular seu fatorial: '))
c = n
mult = 1
print('Calculando {}! :'.format(n))
while c > 0:
    if c > 1:
        print(c, end = ' x ')
    else:
        print(c, end=' = ')
    mult *= c
    c -= 1
print(mult)

