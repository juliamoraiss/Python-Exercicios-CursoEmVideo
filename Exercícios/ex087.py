matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = 0
somaterceira = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        maior = max(matriz[1])
        matriz[l][c] = num
        if c == 2:
            somaterceira += num
        if num % 2 == 0:
            somapares += num
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end =' ')
    print()
print('-='*30)

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maior}')