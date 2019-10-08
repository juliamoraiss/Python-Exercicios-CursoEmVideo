print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO PYCHARM'))
print('=' * 30)
saque = int(input('Qual valor deseja sacar? R$'))
n50 = saque // 50
n50b = saque % 50
n20 = n50b // 20
n20b = n50b % 20
n10 = n20b // 10
n10b = n20b % 10
n1 = n10b // 1
print(f'''Total de:
{n50} cédulas de R$50
{n20} cédulas de R$20
{n10} cédulas de R$10
{n1} cédulas de R$1''')