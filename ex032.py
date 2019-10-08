from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
bi1 = ano % 400
bi2 = ano % 100
bi3 = ano % 4
if bi3 == 0 and bi2 != 0 or bi1 == 0:
    print('{} é um ano BISSEXTO.'.format(ano))
else:
    print('{} não é um ano BISSEXTO'.format(ano))
