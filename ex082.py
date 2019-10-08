lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opcao in 'N':
        break
for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')