from operator import itemgetter
pessoa = dict()
lista = list()
listamulher = list()
somaidades = contmulher = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F: ')
    if pessoa['sexo'] == 'F':
        contmulher =+ 1
        listamulher.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaidades += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite apenas S ou N: ')
    if opcao == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoa(s).')
media = somaidades / len(lista)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: {listamulher}')
print('- Lista das pessoas que estão acima da média: ')
for p in lista:
    if(p['idade']) > media:
        for k, v in p.items():
            print(f'{k} = {v}', end = ' ')
print()
print('----- ENCERRADO -----')


