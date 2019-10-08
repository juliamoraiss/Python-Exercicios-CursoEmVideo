tupla = (int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite um último valor: ')))
print(f'Você digitou os valores {tupla}')
if tupla.count(9) != 0:
    print(f'O valor 9 foi digitado {tupla.count(9)} vez(es)')
else:
    print(f'O valor 9 não foi digitado nenhuma vez')
if 3 in tupla:
    posicao = tupla.index(3) + 1
    print(f'O valor 3 foi digitado na {posicao}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
cont = 0
for p in tupla:
    par = p % 2
    if par == 0:
        cont += 1
if cont == 0:
    print('Nenhum valor par foi digitado')
elif cont != 0:
    print(f'{cont} valores pares foram digitados')

