''' DESAFIO 52:
Faça um programa que leia um número e diga se ele é o não um número primo.
'''

num = int(input("Digite uma número: ")) # coleta um número
t = 0
print()
for c in range(1, num + 1):             # verificando se o número é primo
    if num % c == 0:
        print(f"\033[32m{c}\033[m", end=" ")
        t += 1

    else:
        print(f"\033[31m{c}\033[m", end=" ")

print()
print(f"\n\033[mO número {num} foi dividido {t} vezes.")

if t == 2:                              # resultado
    print("Esse número é primo!!")
else:
    print("Esse número não é primo!!")
