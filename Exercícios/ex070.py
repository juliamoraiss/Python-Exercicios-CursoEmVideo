soma = cont = 0
lista1 = []
lista2 = []
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    print('-' * 20)
    soma += preco
    lista1.append(nome)
    lista2.append(preco)
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).upper()
    if preco > 1000:
        cont += 1
    if opcao == 'N':
        break
maisbarato = min(lista1)
precomaisbarato = min(lista2)
print(f'A soma dos produtos é de R${soma:.2f}')
print(f'{cont} produtos custam mais de R$1000')
print(f'O produto mais barato é o/a {maisbarato} e custa R${precomaisbarato:.2f}')
