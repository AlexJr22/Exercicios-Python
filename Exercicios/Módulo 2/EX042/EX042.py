''' DESAFIO 42:
Reforçando o D35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    -> Equilátero
    -> isóscelas
    -> Escaleno
'''

# coletando os seguimentos
r1 = int(input('Primeiro Seguimento: '))
r2 = int(input('Segundo Seguimento: '))
r3 = int(input('Terciero Seguimento: '))

# verificando se os seguimentos formam um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem forma um triâgulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSELES')
else:
    print('Não pode forma um triângulo')
    