num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão
 [1] converter para BINÁRIO
 [2] converter para OCTAL
 [3] converter para HEXADECIMAL''')

base = int(input('Sua opção: '))

if base == 1:
    print('O binário de {} é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O octal do número {} é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O hexadecimal do número {} é {}'.format(num, hex(num)[2:]))
else:
    print('Digite 1, 2 ou 3 para fazer a conversão desejada.')
