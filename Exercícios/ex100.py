from random import randint
from time import sleep

def sorteio(lista):
    while len(lista) < 5:
        n = randint(1, 10)
        lista.append(n)
    print(f'Sorteando 5 valores da lista:')
    for n in lista:
        print(f'{n}', end=' ')
        sleep(0.5)
    print()
def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares é {soma}')

numeros = list()
sorteio(numeros)
somapar(numeros)
