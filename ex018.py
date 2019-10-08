from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print('O ângulo de {:.2f} graus tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo,sen,cos,tg))
