from datetime import date
print('\033[33mInsira o ano de nascimento do atleta para saber a qual categoria ele pertence\033[m')
anonasc = int(input('\033[4mAno de nascimento:\033[m '))
anohoje = date.today().year
idade = anohoje - anonasc
print('O atleta tem {}'.format(idade))
if idade <= 9:
    print('Categoria \033[31mMIRIM\033[m')
elif idade <= 14:
    print('Categoria \033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria \033[33mJUNIOR\033[m')
elif idade <= 25:
    print('Categoria \033[34mSÊNIOR\033[m')
else:
    print('Categoria \033[35mMASTER\033[m')
