''' DESAFIO 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

n = int(input('Digite um número para saber seu Fatarial: '))
c = n
f = 1
print('O fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
