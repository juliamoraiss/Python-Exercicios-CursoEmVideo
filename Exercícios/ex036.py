from time import sleep
print('\033[33m-'*30)
print('INSIRA SEUS DADOS PARA ANÁLISE')
print('-'*30)
print('\033[m')

valor = float(input('\033[34mQual é o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar? \033[m'))

prestacao = valor / anos / 12
condicao = 30 * salario / 100

print('\033[31mPROCESSANDO...\033[m')
sleep(2)
print('\033[34mPara pagar uma casa de R${:.2f} em {} anos '
      'a prestação mensal será de: R${:.2f}\033[32m'.format(valor, anos, prestacao))

if prestacao <= condicao:
    print('\033[32mParabéns! O empréstimo foi concedido!\033[m')
else:
    print('\033[31mDesculpe, o empréstimo foi negado.\033[m')
