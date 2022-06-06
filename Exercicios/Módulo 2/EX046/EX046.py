''' DESAFIO 46:
Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0 
segundos, com uma pausa de 1 segundo entre eles.
'''

from time import sleep

for t in range(10, 0, -1):  # cronômetro de 10 segundos
    print(t)
    sleep(1)

print('\033[;31mBOOOOOOOOOOOOOOOOOOOOOOOOOOM\033[m')
