print('Insira sua notas para saber se você foi aprovado: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média foi {:.1f}'.format(media))
if media < 5:
    print('Você foi \033[31mREPROVADO\033[m')
elif media >= 7:
    print('Você foi \033[32mAPROVADO\033[m')
else:
    print('Você está de \033[33mRECUPERAÇÃO\033[m')
