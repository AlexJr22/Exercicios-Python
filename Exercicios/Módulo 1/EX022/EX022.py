'''DESAFIO 22:
Faça um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas as letras minúsculas
    - Quantas letras ao todo sem considerar os espaços
    - Quantas letras tem o primeiro nome'''

# coletando os dados e processando eles
nome = str(input('Digite seu nome completo: ')) # recebe o nome
primeiro_nome = nome.split()

# mostrando o resultado
print(f'Olá {primeiro_nome[0]} seu nome com todas as letras maiúsculas é: ', end='')
print(nome.upper())

print(f'Seu nome com todas as letras minúsculas é: ', end='')
print(nome.lower())

print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

print(f'Seu primeiro nome tem {len(primeiro_nome[0])} letras')
