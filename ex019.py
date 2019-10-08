from random import choice
a1 = input('Escreva o nome do 1º aluno: ')
a2 = input('Escreva o nome do 2º aluno: ')
a3 = input('Escreva o nome do 3º aluno: ')
a4 = input('Escreva o nome do 4º aluno: ')
print('O aluno escolhido para apagar o quadro foi {}'.format(choice([a1,a2,a3,a4])))
