s = float(input('Digite o salário: '))
a1 = 10 * s / 100
a2 = 15 * s / 100
if s > 1250:
    print('O aumento do salário será de \033[32mR${:.2f}\033[m. O novo salário será R${:.2f}.'.format(a1, s + a1))
else:
    print('O aumento do salário será de R${:.2f}. O novo salário será R${:.2f}.'.format(a2, s + a2))
