''' DESAFIO 51:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa prograssão.
'''

primeiro = int(input("Primeiro Termo: "))           # primeiro termo da PA
razao = int(input("Razão"))                         # razão da PA
decimo = primeiro + (10 - 1) * razao                # decimo termo
for c in range(primeiro, decimo + razao, razao):
    print("{}".format(c), end=" -> ")
print("ACABOU")
