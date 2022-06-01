'''DESAFIO 27:
Faça um programa que leia o nome de uma pessoa e mostre o primeiro e o ultimo nome dela separadamente
    EX: Ana Maria de Souza
        - Primeiro: Ana
        - Ultimo: Souza'''

# coletando os dados e formatando eles
nome = (str(input('Digite seu nome completo: ')).strip().upper()).split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
