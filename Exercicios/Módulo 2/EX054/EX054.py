''' DESAFIO 54:
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pesooas ainda não atingiram a  maioridade e quantas ja são de maiores.
'''

from datetime import date 


hoje = date.today().year    # data atual do sistema

maior18 = 0 # número de pessoas maiores de idade
menor18 = 0 # número de pessoas menores de idade

for idade in range(0, 7):   # verificando a idade das pessoas
    idade = int(input(f"Em que ano a {idade}º pessoa nasceu? "))
    if hoje - idade >= 18:
        maior18 += 1
    else:
        menor18 += 1

# resultado
print("""{} pessoa(s) analisadas são maiores de idade,
e {} pessoa(s) são menores de idade""".format(maior18, menor18))
