from datetime import date
trabalhador = {'Nome': str(input('Nome: ')),
               'Idade': (date.today().year) - int(input('Ano de Nascimento: ')),
               'Ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if trabalhador['Ctps'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Contratação'] + 35 - (date.today().year) + trabalhador['Idade']
for k, v in trabalhador.items():
    print(f'{k} é {v}')
