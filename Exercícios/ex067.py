while True:
    print('-' * 36)
    n = int(input('Deseja ver a tabuada de qual número: '))
    print('-' * 36)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa encerrado. Até logo!')
