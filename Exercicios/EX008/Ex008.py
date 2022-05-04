'''Desafio 8:
Faça um programa que leia um valor em metros e exiba ele em centimentros e milimetros'''

metro = int(input('Qual a distância em metros: '))  # recebe um valor em metro
centimetro = metro / 100 * 10000                    # converte metros pra CM
milimetro = metro / 1000 * 1000000                  # converte metros pra MM

# resultado da questão 
print(f'{metro} metro convertidos em:')
print(f'CM = {int(centimetro)}')
print(f'MM = {int(milimetro)}')
