from ex108 import moeda

p = float(input('Digite o preço: R$'))
c = moeda.metade(p)

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(c)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 13))}')


