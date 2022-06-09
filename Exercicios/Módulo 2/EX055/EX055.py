''' DESAFIO 55:
Faça uma programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido
'''

menor = maior = 0   # contador de meior e menor peso

for p in range(0, 5):   # validando o meior e menor peso
    peso = int(input("Qual o peso da {}º pessoa?: ".format(p + 1)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

# mostrando o resultado
print(f'O maior peso lido foi {maior}')
print(f'O menos peso lido foi {menor}')
