def metade(n=0, formato=False):
    """
    Calcula a metade do valor informado
    :param n: valor
    :param formato: valor da moeda formato ou não: True ou False
    :return: retorna o resultado de n/2
    """
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


def aumentar(n=0, x=0, formato=False):
    res = ((x / 100) * n) + n
    if formato is False:
        return res
    else:
        return moeda(res)


def diminuir(n=0, x=0, formato=False):
    res = n - ((x / 100) * n)
    if formato is False:
        return res
    else:
        return moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')
