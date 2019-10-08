peso = float(input('Qual é o seu peso (kg)? '))
altura = float(input('Qual é sua altura (m)? '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade.')
else:
    print('Obesidade mórbida')