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

nome = str(input('Nome do atleta:   '))
ano = 