ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = 'S'
while opcao == 'S':
    num = int(input('Digite um número entre 0 e 20: '))
    while num <0 or num >20:
        print('Tente novamente.',end =' ')
        num = int(input('Digite um número entre 0 e 20: '))
    print(f'Voce digitou o número {ext[num]}')
    opcao = str(input('Deseja continuar [S/N]: '))


