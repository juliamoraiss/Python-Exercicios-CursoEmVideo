from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
tupla = (n1, n2, n3, n4, n5)
maior = max(tupla)
menor = min(tupla)
print(f'Os valores sorteados foram: {tupla} ')
print(f'O maior valor sorteado foi o {maior}')
print(f'o menor valor sorteado foi o {menor}')

