'''DESAFIO 18:
Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno°, cosseno°, e tangente desse ângulo'''

from math import radians, cos, sin, tan

angulo = float(input('Digite um ângulo:'))  # recebe o ângulo

seno = sin(radians(angulo)) # calcula senº
cose = cos(radians(angulo)) # calcula cosº
tang = tan(radians(angulo)) # calcula tanº

# resultado
print(f'| ------- O Senº {angulo} é {seno:.2f} ------- |')
print(f'| ------- O Cosº {angulo} é {cose:.2f} ------- |')
print(f'| ------- A tanº {angulo} é {tang:.2f} ------- |')
    