'''DESAFIO 16:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
EX: digite um nÚumero: 6.127
    O número 6.127 tem a parte inteira 6
'''

num1 = float(input('Digite um número: '))   # recebe um número float()
num2 = int(num1)                            # converte o número para int()

# resultado
print(f'A parte inteira de {num1} é {num2}')
