from random import randint
print('-=-'*18)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=-'*18)
n1 = int(input('Em qual número eu pensei? '))
n2 = (randint(0, 10))
cont = 0
while n1 != n2:
    if n1 > n2:
        print('Menos... Tente novamente!')
        n1 = int(input('Em qual número eu pensei? '))
    if n1 < n2:
        print('Mais... Tente novamente!')
        n1 = int(input('Em qual número eu pensei? '))
    cont += 1
    if n1 == n2:
        print('Você acertou depois de {} tentativas! Eu estava mesmo pensando no número {}'.format(cont + 1,n2))
