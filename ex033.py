num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite um terceiro número: '))
if num1 > num2 > num3:
    print('O maior número é o {} e o menor número é o {}'.format(num1,num3))
else:
    if num1 > num3 > num2:
        print('O maior número é o {} e o menor número é o {}'.format(num1, num2))
    if num2 > num1 > num3:
        print('O maior número é o {} e o menor número é o {}'.format(num1, num3))
    if num2 > num3 > num1:
        print('O maior número é o {} e o menor número é o {}'.format(num2, num1))
    if num3 > num1 > num2:
        print('O maior número é o {} e o menor número é o {}'.format(num3, num2))
    if num3 > num2 > num1:
        print('O maior número é o {} e o menor número é o {}'.format(num3, num1))
    if num1 == num2 == num3:
        print('Os números são iguais')
