'''Crie um script que leia o mês e ano de nascimento de uma pessoa e mostre no terminal um mensagem 
com a data formatada'''
from datetime import date

ano = int(input('Qual ano você nasceu?: '))
mes = str(input('Qual o mês você nasceu?: '))
idade = date.today().year - ano

print(f'Você nasceu em {ano} no mês de {mes}')
print(f'Você tem {idade} anos de idade')
