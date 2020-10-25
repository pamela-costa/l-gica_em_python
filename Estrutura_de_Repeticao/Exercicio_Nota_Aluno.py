class Aluno:
    nome = ''
    nota = 0.0
    def passou(self):
        if (self.nota >= 7.0):
            print("PASSOU!!!")
        else:
            print("Reprovado! =(")

qtd = int(input('Quantos alunos a turma tem? '))

aluno = 1
melhor_aluno = Aluno()
#maior_nota = 0
#maior_nome = ''

while aluno <= qtd:
    print(f'Aluno {aluno}')
    a = Aluno()
    a.nome = str(input('Nome do Aluno: '))
    a.nota = float(input('Nota do aluno: ')) 
    #nome_aluno = str(input('Nome do Aluno: '))
    #nota_aluno = float(input('Nota do aluno: ')) 
    aluno = aluno + 1
    if a.nota > melhor_aluno.nota:
        melhor_aluno = a
        #maior_nota = nota_aluno
        #maior_nome = nome_aluno

#print(f'A maior nota {maior_nota} foi do aluno {maior_nome}') 
print(f'A maior nota {melhor_aluno.nota} foi do aluno {melhor_aluno.nome}') 
melhor_aluno.passou()