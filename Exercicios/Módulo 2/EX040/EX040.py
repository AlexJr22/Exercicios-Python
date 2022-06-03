'''DESAFIO 40:
Crie um programa que leia  duas notas de um aluno e calcule sua média, mostrando um mensagem no final, de acordo
com a média atingida:
    -> Média abaixo de 5,0 REPROVADO
    -> Média entre 5,0 e 6,9 RECUPERAÇÃO
    -> Média 7,0 ou acima APROVADO
'''
# dados dos alunos
nome = str(input('Qual o nome do aluno!: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

# resultado das provas

nf = (n1 + n2) / 2 # média do aluno

print('-=-' * 15)
print('RESULTADO DAS PROVAS'.center(45))
print('-=-' * 15)

# resultado
if nf < 5.0:
    print('O aluno {} foi REPROVADO!'.format(nome))
    print('A média do aluno foi {}'.format(nf))
elif nf >= 5.0 and nf < 6.9:
    print('O aluno {} está de RECUPERAÇÃO!'.format(nome))
    print('A média do aluno foi {}'.format(nf))

else:
    print('O aluno {} foi APROVADO'.format(nome))
    print('A média do aluno foi {}'.format(nf))
