'''DESAFIO 26:
Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra 'a'
    - Em qual posição ela aparece pela primeira vez
    - Em qual posição ela aparece pela ultima vez '''

# coletando e processando os dados

frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" aparece {} vezes!'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}!'.format(frase.find('a')+1))
print('A letra "a" aparece pela ultima vez na posição {}!'.format(frase.rfind('a')+1))
