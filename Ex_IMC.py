massa = float(input('Massa (KG): '))
altura = float(input('Altura (M): '))
imc = massa / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if imc < 17:
    print('muito abaixo do peso.')
elif imc >= 17 and imc < 18.5:
    print('Abaixo do peso') 
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 35:
    print('Obesidade')
elif imc >= 35 and imc < 40:
    print('Obesidade Severa')
elif imc > 40:
    print('Obesidade Mórbida')

