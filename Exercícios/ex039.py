from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano

if idade < 18:
    print('Você deverá se alistar daqui {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar esse ano.')
else:
    print('Já passou do tempo de se alistar! Você deveria ter se alistado {} anos atrás.'.format(idade - 18))
