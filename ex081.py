lista = []
opcao = 'S'

while opcao == 'S':
    n = int(input('Digite um valor: '))
    lista.append(n)
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()

print(f'Você digitou {len(lista)} valores.')

lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são: {lista}')

if 5 in lista:
    pos5 = lista.index(5)
    print(f'O valor 5 faz parte da lista e está na {pos5}ª posição!')
else:
    print('O valor 5 não faz parte da lista!')
