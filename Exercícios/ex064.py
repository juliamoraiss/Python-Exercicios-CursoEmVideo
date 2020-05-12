n = 0
soma = 0
cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('A soma dos {} números foi: {}'.format(cont, soma))
