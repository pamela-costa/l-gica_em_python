nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

print(f'A média do aluno é {media:.2f}') 

if media >= 7:
    print('Aluno Aprovado')
else:
    if media >= 5 and media < 7:
        print('Aluno em recuperação')
    else:
        print('Aluno Reprovado')

