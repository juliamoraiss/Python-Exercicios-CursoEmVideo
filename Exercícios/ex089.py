lista = list()
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cont += 1
    lista.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N]:  ')).upper()
    if opcao == 'N':
        break
print('-='*30)
print('{:<3} {} {:>15}'.format('Nº','NOME','MÉDIA'))
print('-'*25)
for c, a in enumerate(lista):
    print(f'{c}', end = '  ')
    print('{:10}'.format(a[0]), end = '')
    print('{:>12.1f}'.format(a[2]))
print('-' * 25)
while True:
    opcao2 = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if opcao2 == 999:
        print('FINALIZANDO...')
        break
    print(f'As notas de {lista[opcao2][0]} são {lista[opcao2][1]}')
    print('-' * 30)
print('VOLTE SEMPRE!')