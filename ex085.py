valores = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
print(f'Os valores pares são: {(sorted(valores[0]))}')
print(f'Os valores ímpares são: {(sorted(valores[1]))}')

