from time import sleep
print('='*43)
print('DIGITE 2 VALORES E ESCOLHA A OPÇÃO DESEJADA')
print('='*43)
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opcao = 0

while opcao != 5:
    print('''=========================
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] DIGITAR NOVOS VALORES
[5] SAIR
=========================''')
    opcao = int(input('Escolha a opção desejada: '))
    if opcao == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1+n2))
        sleep(1)
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é o {}'.format(n1, n2, n1))
            sleep(1)
        else:
            print('Entre {} e {} o maior valor é o {}'.format(n1, n2, n2))
            sleep(1)
    elif opcao == 4:
        sleep(1)
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
if opcao == 5:
    sleep(1)
    print('ATÉ LOGO :*')
