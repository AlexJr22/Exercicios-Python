'''
Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo 
usuario. O programa será interrompido quando o número soliciatado for negativo.
'''

print('''
-=-=-=-=-=-=-=-=-=-=
 Gerador de Tabuada
-=-=-=-=-=-=-=-=-=-=
''')

num = int(input('''Digite um número para ver sua tabuada
>>> '''))

print('-=-=-=-=-=-=-=-=-=-=-=-=')
for n in range(1, 10):
  print(f'{num} X {n} = {num * n}'.center(24))
print('-=-=-=-=-=-=-=-=-=-=-=-=')