''' DESAFIO 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso estaja errado peça a digiteção novamente até ter um valor correto.
'''

# coletando o sexo da pessoa
sexo = str(input('Imforme seu sexo:[M/F] ')).strip().upper()[0]

# validando as informações
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor imforme seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'MASCULINO'
else:
    sexo = 'FEMININO'

# mostrando os dados
print(f'Sexo {sexo} registrado com sucesso')
