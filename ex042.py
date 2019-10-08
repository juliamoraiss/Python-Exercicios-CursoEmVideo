from math import fabs
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if fabs(r2 - r3) < r1 < (r2 + r3):
    print('As retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo será EQUILÁTERO')
    elif r1 == r2 != r3:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 == r3:
        print('O triângulo será ISÓCELES')
    elif r2 != r3 == r1:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 != r3 != r1:
        print('O triângulo será ESCALENO')
elif fabs(r1 - r3) < r2 < (r1 + r3):
    print('As retas podem formar um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo será EQUILÁTERO')
    elif r1 == r2 != r3:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 == r3:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 != r3:
        print('O triângulo será ESCALENO')
elif fabs(r1 - r2) < r3 < (r1 + r2):
    if r1 == r2 == r3:
        print('O triângulo será EQUILÁTERO')
    elif r1 == r2 != r3:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 == r3:
        print('O triângulo será ISÓCELES')
    elif r1 != r2 != r3:
        print('O triângulo será ESCALENO')
    print('As retas podem formar um triângulo!')
else:
    print('As retas NÃO podem formar um triângulo.')