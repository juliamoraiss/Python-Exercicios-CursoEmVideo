p = float(input('Digite o valor do produto: R$'))
desc = p * 0.95
desc2 = p - desc
print('O valor com 5% de desconto é: R${:.2f}. Um desconto de R${:.2f}'.format(desc,desc2))
