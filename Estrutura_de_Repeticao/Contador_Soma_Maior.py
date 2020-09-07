# Contar de 0 até onde a usuário quiser - ler 10 números e soma-los "Somador Numerico"

contador = 1
soma = 0
maior = 0
while contador <= 5:
    num = int(input(f'Digite o {contador}o. valor: '))
    if num > maior:
        maior = num
    soma = soma + num
    contador = contador + 1
print(f'A soma de todos os valores foi {soma}.')
print(f'O maior valor digitado foi {maior}.')

  
