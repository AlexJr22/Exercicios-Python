''' DESAFIO 56
DeseNvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do 
grupo. Qual é o homen mais velho. Quantas mulheres tem no grupo.
'''

idade = homenvelho = num_mulheres = 0
n_homemV = ''

for g in range(0, 4):

    nome = str(input('Qual o nome da {}º pessoa?: '.format(g + 1)))
    idade1 = int(input('Quantos anos a {}º pessoa tem?: '.format(g + 1)))
    sexo = int(input('''qual o sexo da {}º pessoa: 
    [ 1 ] homem
    [ 2 ] mulher\n'''.format(g + 1)))

    if sexo == 1:
        sexo = 'homem'
        if idade1 > homenvelho:
            homenvelho = idade1
            n_homemV = nome
    elif sexo == 2:
        sexo = 'mulher'
        num_mulheres += 1
    idade += idade1

print('A idade média do grupo é {}'.format(idade / 4))
print('O homem mais velho do grupo é {} e ele tem {} anos de idade'.format(n_homemV, homenvelho))
print('A {} mulhere(s) nesse grupo'.format(num_mulheres))
