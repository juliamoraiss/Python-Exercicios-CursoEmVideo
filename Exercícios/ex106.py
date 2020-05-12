def sistema(com):
    help(com)


def título(msg, cor=0):
    tam = len(msg) + 2
    print('\033[m~'*tam)
    print(msg)
    print('~'*tam)
    print('\033[m')

com = ''
while True:
    título('  SISTEMA DE AJUDA PyHELP',32)
    com = str(input('Função ou biblioteca > '))
    if com.upper() == 'FIM':
        título('VOLTE LOGO!')
        break
    sistema(com)

