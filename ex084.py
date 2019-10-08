grupo = list()
pessoa = list()
maiorpeso = menorpeso = 0
maispesado = list()
maisleve = list()
while True:
    nome = str(input('Nome: '))
    pessoa.append(nome)
    peso = float(input('Peso: '))
    pessoa.append(peso)
    if len(grupo) == 0:
        maiorpeso = pessoa[1]
        menorpeso = pessoa[1]
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
    grupo.append(pessoa[:])
    pessoa.clear()
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print(f'Você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi {maiorpeso}. Peso de ', end='')
for p in grupo:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]',end=' ')
print()
print(f'O menor peso foi {menorpeso}. Peso de ', end='')
for p in grupo:
    if p[1] == menorpeso:
        print(f'[{p[0]}]',end=' ')
