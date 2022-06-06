'''DESAFIO 47:
Crie um programa que mostre na tela todos os números pares no intervalo de 1 a 50.
'''

from time import sleep

print('Os números pares entre 1 e 50 são!')
sleep(1.3)

print()
for num in range(0,51,+2):
    print(num, end=' ')
