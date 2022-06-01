'''DESAFIO 19:
Um professor quer sortea um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos 
alunos e escrevendo o nome deles e o nome do escolhido.'''

from random import choice

alunos = []
for v in range(0, 4):   # pergunta o nome dos alunos
    alunos.append(str(input(f'Nome do {v+1}º aluno: ')))

# resultado
print(choice(alunos))   # sorteia um aluno aleatorio
