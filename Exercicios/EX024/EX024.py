'''DESAFIO 24:
Crie um programa que leia o nome de uma cidade e mostre na tela se ela começa ou não com 
"Santa"'''

# coletando o os dados
cidade = str(input('Qual o nome da sua cidade?: ')).strip().split()

# mostrando o resultado no terminal
if cidade[0] == 'santa':
    print('\033[33mSua cidade começa com "santa"!\033[m')
else:
    print('\033[31mSua cidade não começa com "santa"!\033[m')
