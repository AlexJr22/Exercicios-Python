'''DESAFIO 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    -> Se ele ainda vai se alistar ao serviço militar
    -> Se é a hora de se alistar
    -> Se ja passou do tempo do alistamento
Seu programa tambem devera mostra o tempo que falta ou que passou do prazo
'''

from datetime import date

# dados do usuário
hoje = date.today().year
nasc = int(input('Qual o ano que você nasceu: '))
idade = hoje - nasc

# resultado da pesquisa
if idade == 18:
    print('Está na hora de você se alistar!')
elif idade < 18:
    print('Ainda não esta na hora de você se alistar')
    temp1 = 18 - idade
    print('Falta {} anos para você se alistar'.format(temp1))
else:
    print('Já passou do tempo de você se alistar!')
    temp2 = idade - 18
    print('Jà passou {} anos da data do seu Alistamento!'.format(temp2))
