'''DESAFIO 20:
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem de aprensentação'''

from random import shuffle

# coletando o nome dos alunos
a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
turma = [a1, a2, a3, a4]    # quanda o nome de todos os alunos
shuffle(turma)              # embaralha os itens da lista

# resultado
print('A ordem de apresentação dos trabalhos é: ')
for v in range(len(turma)):
    print(f'{v+1}º aluno: {turma[v]}')
