#Contagem Inteligente

inicio = int(input('Qual o numero de inicio? '))
fim = int(input('Qual o número final? '))
 
print('='*30)
print('Contando')
print('='*30)


if inicio < fim:
   while inicio <= fim:
       print(inicio, end='.. ')
       inicio = inicio + 1 
else:
    while fim <= inicio:
        print(inicio, end='.. ')
        inicio = inicio - 1
