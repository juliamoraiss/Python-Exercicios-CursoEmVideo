cont18 = conth = contm = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    opcao = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo [M/F]: ')).upper()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('-' * 30)
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm20 += 1
    if opcao == 'N':
        break
print(f'{cont18} pessoas tem mais de 18 anos.')
print(f'{conth} homens foram cadastrados.')
print(f'{contm20} mulheres tem menos de 20 anos.')
