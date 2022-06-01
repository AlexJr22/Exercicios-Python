'''DESAFIO 25:
Faça um programa que leia o nome de uma pessoa e mostre no terminal se ela tem silva no nome'''

# coletando os dados da pessoa e processando eles
nome = str(input('Digite o nome de uma pessoa: ')).strip().split()
resp = False
for v in range(len(nome)):
    if nome[v].lower() == 'silva':
        print('SIM!! Essa pessoa tem "Silva" no nome!')
        resp = True
        break
    
if resp == False:
    print('NÃO!! Essa pessoa não tem "Silva" no nome!')
