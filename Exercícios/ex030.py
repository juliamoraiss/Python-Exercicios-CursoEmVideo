num = int(input('\033[35mDigite um número inteiro: \033[m'))
resto = (num%2)
cores = {'azul':'\033[34m',
         'limpa':'\033[m'}
if (resto) == 0:
    print('O número {} é {}PAR'.format(num, cores['azul']))
else:
    print('O número {} é {}ÍMPAR'.format(num, cores['azul']))
