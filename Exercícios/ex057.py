sexo = 'F'
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Opção incorreta. Tente novamente!')
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
