from time import sleep
def maior(* num):
    cont = 0
    print(f'Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.5)
        cont += 1
    print(f': Foram informados {cont} valores ao todo.')
    if cont > 0:
        print(f'O maior valor é o {max(num)}')
    else:
        print('O maior valor encontrado foi 0')
    print('-='*20)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()