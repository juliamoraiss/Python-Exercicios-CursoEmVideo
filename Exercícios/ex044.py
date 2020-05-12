precoa = float(input('Qual é o valor do produto? R$'))
print('''Selecione a opção de pagamento:
[1] À vista no dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] Em 3x ou mais no cartão (20% de juros)''')
opcao = int(input('Opção: '))

if opcao == 1:
    precob = precoa * 0.9
elif opcao == 2:
    precob = precoa * 0.95
elif opcao == 3:
    precob = precoa
else:
    precob = precoa * 1.2
print('Preço a pagar: R${}'.format(precob))
