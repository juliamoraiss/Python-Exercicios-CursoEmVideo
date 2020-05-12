dist = float(input('Qual é a distância da viagem em Km? '))
if dist <= 200:
    p = 0.5 * dist
else:
    p = 0.45 * dist
print("Sua passagem custará R${}".format(p))
print('Boa viagem!')