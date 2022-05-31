'''DESAFIO 33:
Faça um programa que leia 3 números e mostre qual é o maior e o menor.
'''

# coletando os números 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
n3 = int(input('Digite um ultimo número: '))

# validando o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# validando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# mostrando os resultados
print('-='*15)
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
print('-='*15)
