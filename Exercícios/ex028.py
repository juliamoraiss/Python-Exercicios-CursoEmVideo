from random import randint
from time import sleep
print('-=-'*18)
print('Vou pensar em um número de 1 a 5. Tente adivinhar...')
print('-=-'*18)
n1 = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
n2 = (randint(0, 5))
if (n1 > 5):
    print('O número deve ser entre 0 e 5')
else:
    if (n1 == n2):
        print('Parabéns! Eu estava mesmo pensando no número {}!'.format(n2))
    else:
        print('GANHEI!! Eu pensei no número {} e não no {}.'.format(n2, n1))
print('Jogue novamente!')
