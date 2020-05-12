from time import sleep
def contador(a, b, c):
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c == 0 and a > b:
        for num in range(a, b - 1, -1):
            print(num, end=' ')
            sleep(0.3)
        print('FIM!')
    if c == 0 and a < b:
        for num in range(a, b + 1, 1):
            print(num, end=' ')
            sleep(0.3)
        print('FIM!')
    if a > b and c > 0:
        for num in range(a, b - 1, -c):
            print(num, end=' ')
            sleep(0.3)
        print('FIM!')
    if a < b and c > 0:
        for num in range(a, b + 1, c):
            print(num, end=' ')
            sleep(0.3)
        print('FIM!')
    if c < 0:
        for num in range(a, b + c, c):
            print(num, end=' ')
            sleep(0.3)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contador(a, b, c)