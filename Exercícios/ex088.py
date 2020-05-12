from random import randint
from time import sleep
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('{:^35}'.format(f'SORTEANDO {jogos} JOGOS'))
numeros = []
for c in range(1, (jogos + 1)):
    for n in range(0, 6):
        sorteado = randint(1, 60)
        while sorteado in numeros:
            sorteado = randint(1, 60)
        if sorteado not in numeros:
            numeros.append(sorteado)
    print(f'Jogo {c}: {sorted(numeros)}')
    numeros.clear()
    sleep(1)
print('{:^35}'.format('BOA SORTE!'))