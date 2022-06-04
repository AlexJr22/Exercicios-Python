''' DESAFIO 41:
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
cartegoria, de acordo com idade:
    -> até 9 anos: mini
    -> até 14 anos: infantil
    -> até 19 anos: junior
    -> até 20 anos: sénior
    -> Acima: master
'''

from datetime import date

# Dados do atleta 
nome = str(input('Nome do atleta: '))
ano = int(input('Em quel ano ele nasceu: '))

hoje = date.today().year    # recebe o ano atual
idade = hoje - ano          # calcula a idade do atleta

# Resultado da pesquisa
print('-=-' * 20)
print('                 CATEGORIA DO ATLETA {}'.format(nome.upper()))
print('-=-' * 20)

if idade < 9:
    print(f'Este atleta tem {idade} anos e sua categoria é MINI!')
elif idade < 14:
    print(f'Este atleta tem {idade} anos e sua categoria é INFANTIL')
elif idade < 19:
    print(f'Este atleta tem {idade} anos e sua categoria é JUNIOT')
elif idade <= 20:
    print(f'Este atleta tem {idade} anos e sua categoria é SENIOR')
else:
    print(f'Este atleta tem {idade} anos e sua categoria é MASTER')
