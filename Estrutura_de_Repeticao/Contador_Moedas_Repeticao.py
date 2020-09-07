def cotacao_dolar():
    return 5.39

dolar = cotacao_dolar()

contador = 1 
qtd = int(input('Quantas vezes você deseja converter? '))
while contador <= qtd:
    real = float(input('Qual o valor em R$ ?'))
    conversao = real / dolar
    print(f'O valor convertido em dolar é {conversao:.2f}')
    contador = contador + 1 
