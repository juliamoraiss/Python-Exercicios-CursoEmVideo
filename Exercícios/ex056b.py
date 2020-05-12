somaidades = 0
totalpessoas = 0
totalm20 = 0
idadehomemmaisvelho = 0
homemmaisvelho = ''
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): ')).upper()
    somaidades += idade
    totalpessoas += 1
    if sexo == 'F' and idade < 20:
        totalm20 += 1
    if sexo == 'M':
        if p == 1:
            idadehomemmaisvelho = idade
            homemmaisvelho = nome
        if idade > idadehomemmaisvelho:
            idadehomemmaisvelho = idade
            homemmaisvelho = nome
media = somaidades / totalpessoas
print('A média de idade do grupo é {}'.format(media))
print('{} mulher(es) tem menos que 20 anos'.format(totalm20))
print('O {} é o homem mais velho e tem {} anos'.format(homemmaisvelho,idadehomemmaisvelho))
