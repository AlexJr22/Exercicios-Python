'''DESAFIO 38:
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    -> O primeiro número é maoir
    -> O segundo número e maior
    -> Não existe valor maior
'''

# coletando os dois números
num1 = int(input('Diga um número: '))
num2 = int(input('Diga outro número: '))

# validando os dois números
if num1 > num2:
    print('O número {} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que {}'.format(num2, num1))
else:
    print('Os dois números tem o mesmo valor')
