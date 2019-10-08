def metade(n=0):
    res = n/2
    return res

def dobro(n=0):
    res = n*2
    return res

def aumentar(n=0, x=0):
    res = ((x/100) * n) + n
    return res

def diminuir(n=0, x=0):
    res = n - ((x/100) * n)
    return res

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')