from random import randint
from time import sleep
print('\033[33m-='*22)
print('\033[36mVamos brincar de PEDRA, PAPEL E TESOURA? =D\033[m')
print('\033[33m-='*22)
print('\033[m')

print('''\033[34mEscolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m\n''')
opcao = int(input('\033[36mQual é sua jogada? : \033[m'))
sleep(1)
print('\033[7;31m{0:^6}\033[m'.format('JO'))
sleep(1)
print('\033[7;31m{0:^6}\033[m'.format('KEN'))
sleep(1)
print('\033[7;31m{0:^6}\033[m\n'.format('PÔ'))
sleep(1)
itens = ('PEDRA','PAPEL','TESOURA')
pc = randint(0,2)

if pc == 0:
    if opcao == 0:
        print('\033[32mEu escolhi PEDRA. Empatou!')
    elif opcao == 1:
        print('\033[32mEu escolhi PEDRA. Você ganhou!')
    elif opcao == 2:
        print('\033[32mEu escolhi PEDRA. Empatou!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2 and opcao == 1:
    print('\033[32mEu escolhi PAPEL. Eu ganhei!')
elif pc == 2 and opcao == 2:
    print('\033[32mEu escolhi PAPEL. Empatou!')
elif pc == 2 and opcao == 3:
    print('\033[32mEu escolhi PAPEL. Você ganhou!')
elif pc == 3 and opcao == 1:
    print('\033[32mEu escolhi TESOURA. Você ganhou!')
elif pc == 3 and opcao == 2:
    print('\033[32mEu escolhi TESOURA. Eu ganhei!')
elif pc == 3 and opcao == 3:
    print('\033[32mEu escolhi TESOURA. Empatou!')