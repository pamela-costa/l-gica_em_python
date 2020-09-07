#Contagem simples 0 até 10

contador = 0
while contador <= 10:
    print(contador)
    contador = contador + 1
print('terminei de contar')

# Contagem Regressiva

contador = 10
while contador >= 0:
    print(contador)
    contador = contador - 1
print('contagem finalizada')

# Usuário decide até onde quer contar

num = int(input('Quer contar até quanto? '))
contador = 0
while contador <= num:
    print(contador)
    contador = contador + 1
print('terminei de contar')

#Usuário decide quantos números quer saltar na contagem


valor = int(input('Quer contar até quanto? '))
salto = int(input('Quer saltar quantos números? '))
contador = 0
while contador <= valor:
    print(contador)
    contador = contador + salto
print('terminei de contar')