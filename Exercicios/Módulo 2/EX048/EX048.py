''' DESAFIO 48:
Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no 
intervalo de 1 ate 500.
'''

c = 0
for num in range(1,500+1,+2):   # valida se o número é impar e multiplo de 3
    if num % 3 == 0:
        c += num
print(c)
