frase = str(input('Digite uma frase para saber se ela é um PALÍNDROMO: ')).replace(" ","").upper().strip()
comp = len(frase)
inverso = ''
for letra in range(comp - 1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('O inverso de {} é {}. É PALÍDROMO'.format(inverso, frase))
else:
    print("A frase digitada não é um PALÍNDROMO!")
