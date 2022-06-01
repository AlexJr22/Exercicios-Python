'''DESAFIO 28:
Faça um programa que faça o computador pensar em um número entre 0 e 5 e depois peça pro usuario tentar adivinhar o número.'''

from random import randint

num = randint(0, 5) # pensando em um número 
resp = int(input('Eu pensei em um número entre 0 e 5 você consegui adivinhar?: ')) # resposta do usuario

# validado a resposta do usuario
if resp == num:
    print('PARABENS, você acertou!!!!')
else:
    print(f'NÃO FOI DESSA VEZ, eu pensei no número {num}!!!')
