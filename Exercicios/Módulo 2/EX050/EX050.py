''' DESAFIO 50:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar, desconsidere-o.
'''

num = 0
for n in range(1, 7):   # coletando os 7 números
    n1 = int(input("Digite o {} número: ".format(n)))
    if n1 % 2 == 0:
        num += n1
print("A soma dos números pares é: {}".format(num))
