'''DESAFIO 17:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
e calcule sua hipotenusa.'''

from math import hypot

co = float(input('Qual o valor do cateto oposto: '))    # recebe o cateto oposto
ca = float(input('Qual o valor do cateto adjacente: ')) # recebe o cateto adjacente
hipot = hypot(co, ca)   # calcula a hipotenusa

# resultado
print(f'A hipotenusa desse triângulo retângulo é {hipot:.2f}.')
