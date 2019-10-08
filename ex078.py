lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c + 1}: '))
    lista.append(n)
print(f'Você digitou os valores: {lista}')
maior = max(lista)
posmaior = []
menor = min(lista)
posmenor = []
for c, v in enumerate(lista):
    if v == maior:
        posmaior.append(c + 1)
for c2, v in enumerate(lista):
    if v == menor:
        posmenor.append(c2 + 1)
print(f'O maior valor digitado foi o {maior} na(s) posição(ões) {posmaior}')
print(f'O menor valor digitado foi o {menor} na(s) posição(ões) {posmenor}')
