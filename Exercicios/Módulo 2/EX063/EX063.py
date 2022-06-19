'''DESAFIO 63:
Escreva um programa que leia um número inteiro qualquer e mostre na tela Os N primeros elementos de uma sequencia fibo
'''

print('-='*15)
print('Sequencia de Fibonacci')
print('-='*15)

n = int(input('Quantos termos você quer mostrar?: '))

t1 = 0 
t2 = 1
print('~'*100)
print(f'{t1} -> {t2}', end=' -> ')

cont = 3
while cont <= n:
  t3 = t1 + t2
  print(f'{t3}', end=' -> ')
  t1 = t2
  t2 = t3
  cont += 1
  
print('FIM')
print('~'*100)
