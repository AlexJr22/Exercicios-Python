'''DESAFIO 13:
Faça um programa que leia o sálario de um funcionario e mostre seu novo sálario com, com 15% de aumento.'''
salario_inic = float(input('Qual o sálario atual do do funcionario?: R$'))# recebe o sálario inicial
nov_salario = salario_inic + (salario_inic * 15/100)                    # adiciona o aumento 

# resultado
print(f'O novo sálario do é R${nov_salario:.2f}')