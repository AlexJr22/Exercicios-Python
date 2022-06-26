''' Desafio 67:
Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuario. 
O programa será interrompido quandoo número soliciatado for negativo.
'''


print('-='* 20)
print('Gerador de Tabuada'.center(40))
print('-='* 20)

while True:
  print('Para encerrar o programa digite um número negativo!')
  num = int(input('Digite um número para ver sua tabuada: '))

  if num < 0:
    print('Programa finalizado!')
    break

  else:
    for v in range(1, 10):
      print(f'{num} x {v} = {num*v:>2}')
