'''
Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo 
usuario. O programa será interrompido quando o número soliciatado for negativo.
'''
from time import sleep

print('''
-=-=-=-=-=-=-=-=-=-=
 Gerador de Tabuada
-=-=-=-=-=-=-=-=-=-=
''')

while True:
  num = int(input('''Digite um número para ver sua tabuada
>>> '''))
  if num == 0:
    print('ENCERRANDO ...')
    sleep(1.3)
    break
  else:
    print('-=-=-=-=-=-=-=-=-=-=-=-=')
    for n in range(1, 10):
      print(f'{num} X {n} = {num * n}'.center(24))
    print('-=-=-=-=-=-=-=-=-=-=-=-=')
  
print('Volte Sempre!!')
