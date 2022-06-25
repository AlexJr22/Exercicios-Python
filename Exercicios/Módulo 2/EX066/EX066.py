''' Desafio 66:
Crie um programa que leia varios números pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999. Que é a condição de parada. no final mostre quantos 
números foram digitados e qual foi a soma entre eles.
'''
stop = cont = sumNunbers = 0
while stop != 999:
  num = int(input('Digite um número: [999 para parar]'))
  if num == 999:
    stop = 999

  else:
    cont += 1
    sumNunbers += num

print('-=' * 15)
print(f'Foram digitados ao todo {cont} números')
print(f'A soma entre ele é {sumNunbers}')
print('-=' * 15)
