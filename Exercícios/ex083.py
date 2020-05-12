exp = str(input('Digite a expressão: '))
lista = []
abertos = 0
fechados = 0
for indice in range(0, len(exp)):
    elemento = exp[indice]
    anterior = exp[indice - 1]
    lista.append(elemento)
    if elemento == '(':
        abertos += 1
    if elemento == ')':
        fechados += 1
        if fechados > abertos or anterior in '+-*/':
            print('Sua expressão não é válida')
            break
if abertos != fechados or lista[-1] in '+-*/':
    print('Sua expressão não é válida')
else:
    print('Sua expressão é válida')


