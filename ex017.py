from math import hypot
co = float(input('Qual é o comprimento do cateto oposto do triângulo? '))
ca = float(input('Qual é o comprimento do cateto adjacente do triângulo? '))
print('O comprimento da hipotenusa do triângulo é {:.2f}'.format(hypot(co,ca)))
