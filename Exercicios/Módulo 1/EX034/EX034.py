'''DESAFIO 34:
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios acima de R$1250,00 calcule um aumento de 10% para os inferiores ou iguais o aumento é de 15%
'''

salario = float(input('Digite seu o valor do seu salário:')) # coletando o sálario 

if salario < 1250.00:   # aumentando o salário em 15%
    ns = salario + (salario * 0.15)
    print(f'Seu salário com 15% de aumento é: R${ns:.2f}')
else:                   # aumentando o salário em 10%
    ns2 = salario + (salario * 0.10)
    print(f'Seu novo salário com 10% de aumento é: R${ns2:.2f}')
