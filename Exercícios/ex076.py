print('='*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
        'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)
for p in range(0, len(listagem), 2):
    print('{:.<30}'.format(listagem[p]), end=' ')
    print('R$ {:>6.2f}'.format(listagem[p+1]))
