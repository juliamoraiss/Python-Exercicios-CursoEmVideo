palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} temos ', end = '')
    for letra in palavras[c]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
