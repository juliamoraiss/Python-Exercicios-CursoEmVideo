vel = float(input('Qual é a velocidade atual do carro? '))
multa = (vel-80)*7
if vel > 80:
    print('\033[31mVocê ultrapassou o limite permitido e por isso foi multado!\033[m')
    print('\033[31mSua multa custará\033[m \033[33mR${}\033[m'.format(multa))
print('\033[32mSiga viagem!\033[m')
