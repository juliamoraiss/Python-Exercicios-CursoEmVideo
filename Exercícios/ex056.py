listaidade = []
listaidadem = []
listam = []
cont = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M/F): '))
    listaidade.append(idade)
    if sexo == 'M':
        listaidadem.append(idade)
        if idade == max(listaidadem) and p == 1:
            maxidadem = max(listaidadem)
            listam.append(nome)
    if sexo == 'F' and idade < 20:
        cont += 1
maxidadem = max(listaidadem)
media = sum(listaidade) / len(listaidade)
print('A média de idade desse grupo é de {} anos'.format(media))
print('O homem mais velho do grupo é o {} e ele tem {} anos'.format(listam, maxidadem))
print('{} mulher(es) tem menos de 20 anos'.format(cont))
