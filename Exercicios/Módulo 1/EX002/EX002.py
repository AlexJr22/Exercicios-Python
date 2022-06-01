'''DESAFIO 2:
Crie um script que leia o mês e ano de nascimento de uma pessoa e mostre no terminal um mensagem 
com a data formatada'''

from datetime import date

ano = int(input('Qual ano você nasceu?: '))     # variavel que recebe o ano de nascimento
mes = str(input('Qual o mês você nasceu?: '))   # variavel que recebe o mês de nascimento
idade = date.today().year - ano                 # variavel que calcula a idade do usuario

print(f'Você nasceu em \033[34m{ano}\033[m no mês de \033[34m{mes}\033[m')
print(f'Você tem \033[34m{idade}\033[m anos de idade')
