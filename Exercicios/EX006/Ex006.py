'''Crie um algoritimo que leia um número e mostre seu dobro, triplo, e raiz quadrada'''
from math import sqrt

num = int(input('Digite um número: ')) # Recebe um valor pelo teclado

# calculando o dobro
print(f'O dobro de {num} é {num*2}!')

# calculando o triplo
print(f'O triplo de {num} é {num*3}!')

# calculando a raiz quadrada usando a biblioteca math
print(sqrt(num))
