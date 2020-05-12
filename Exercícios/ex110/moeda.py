def metade(n=0, formato=False):
    res = n / 2
    if formato is False:
        return res
    else:
        return moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    if formato is False:
        return res
    else:
        return moeda(res)


def aumentar(n=0, tx=0, formato=False):
    res = ((tx / 100) * n) + n
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir(n=0, tx=0, formato=False):
    res = n - ((tx / 100) * n)
    if formato is False:
        return res
    else:
        return moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n, tx1, tx2):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{tx1}% de aumento: \t{aumentar(n, tx1, True)}')
    print(f'{tx2}% de redução: \t{diminuir(n, tx2, True)}')
    print('-'*30)