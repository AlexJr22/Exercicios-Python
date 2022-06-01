'''DESAFIO 35:
Crie um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triângulo
'''

print('=x=' * 15)
print('ANALISANDO TRIÂNGULOS')
print('=x=' * 15)
# coletando os dados
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo seguimento'))
r3 = float(input('Terceiro seguimento'))

# processando os dados
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos PODEM formar um triângulo ')
else:
    print('Esses seguimentos NÃO podem formar um triângulo')
