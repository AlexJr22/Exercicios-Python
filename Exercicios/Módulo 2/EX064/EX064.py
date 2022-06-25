'''DESAFIO 64:
Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, 
que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag
'''


num = cont = soma = 0

while num != 999:
  num = int(input('Digite um número: [digite 999 para parar]'))
  soma += num
  cont += 1
  
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - 999}')
print('ACABOU')