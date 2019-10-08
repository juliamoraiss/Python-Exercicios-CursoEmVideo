n = int(input('Digite um número: '))
print('A tabuada do número {} é:'.format(n))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n*c)))
