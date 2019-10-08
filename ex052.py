num = int(input('Digite um número: '))
total = 0
for c in range(1, (num + 1)):
    if num % c == 0:
        total += 1
if total == 2 and num > 2:
    print('É um número primo')
else:
    print('Não é um número primo')
