def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorail de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return f


print(fatorial(5, True))
help(fatorial)
