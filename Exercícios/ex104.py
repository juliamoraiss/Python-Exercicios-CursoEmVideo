def leiaint(msg):
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
           num = int(n)
           break
        else:
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
    return num


n = leiaint('Digite um número: ')
print(f"Você acabou de digitar o número {n}")
