'''DESAFIO 9:
Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
'''

num = int(input('Digite um número para ver sua tabuada: ')) # recebe um número inteiro
print('-='*30)
for v in range(0, 10):
    print(f'|       \033[33m{num} X {v} = {num*v:2d}\033[m        |'.center(60))
    