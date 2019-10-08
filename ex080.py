lista = []
for c in range(0, 5):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if c == 0 or n > (lista[-1]):
        lista.append(n)
        print('Adicionado ao final da lista')
    elif n < min(lista):
        lista.insert(0, n)
        print('Adicionado a posição 0 da lista')
    else:
        lista.insert(1, n)
        print('Adicionado a posição 1 da lista')


print(lista)
