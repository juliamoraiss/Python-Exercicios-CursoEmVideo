def leiaint(msg):
    while True:
        try:
            numi = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido. \033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar o valor.\033[m')
            return 0
        else:
            return numi


def leitfloat(msg):
    while True:
        try:
            numr = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número real válido. \033[m')
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar o valor.\033[m')
            return 0
        else:
            return numr


n = leiaint('Digite um número inteiro: ')
n2 = leitfloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o real {n2}')