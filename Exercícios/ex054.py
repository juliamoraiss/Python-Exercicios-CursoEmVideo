from datetime import date
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = anoatual - anonasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas já são MAIORES de idade'.format(maior))
print('{} pessoas ainda NÃO atingiram a maioridade'.format(menor))
