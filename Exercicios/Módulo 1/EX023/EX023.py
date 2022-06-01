'''DESAFIO 23:
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

EX:Digite um número: 1834
    - unidade:  4
    - dezena:   3
    - centena:  8
    - milhar:   1'''

# coletando os dados e processando eles
num = int(input('Digite um número: '))
unid = num // 1 % 10        # unidade
deze = num // 10 % 10       # dezena 
cent = num // 100 % 10      # centena
milh = num // 1000 % 10     # unidade de milhar

# mostrando o resultado
print('-=' * 16)
print(f'|->   Unidade: \033[33m{unid:>16}\033[m')
print(f'|->   Dezana: \033[33m{deze:>17}\033[m')
print(f'|->   Centena: \033[33m{cent:>16}\033[m')
print(f'|->   Unidade de milhar: \033[33m{milh:>6}\033[m')
print('-=' * 16)
