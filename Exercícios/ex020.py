from random import shuffle
a1 = input('Escreva o nome do 1º aluno: ')
a2 = input('Escreva o nome do 2º aluno: ')
a3 = input('Escreva o nome do 3º aluno: ')
a4 = input('Escreva o nome do 4º aluno: ')
alunos = [a1,a2,a3,a4]
shuffle(alunos)
print('A ordem das apresentações é: ')
print(alunos)
