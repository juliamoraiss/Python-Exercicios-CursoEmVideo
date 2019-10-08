opcao = 'S'
soma = 0
cont = 0
lista = []
while opcao == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    lista.append(n)
    opcao = str(input('Deseja continuar? [S/N]: ')).upper()
media = soma / cont
print('A média entre os valores foi de {:.2f}'.format(media))
print('O maior valor foi o {} e o menor valor o {}'.format(max(lista), min(lista)))
