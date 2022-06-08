''' DESAFIO 53:
Crie um programa que leia uma frase qualquer e diga se ela é o não um palíndromo, desconsiderando os espaços.
'''

frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = ""
for letra in range(len(junto) - 1, -1 , -1):
    inverso += junto[letra]
print(junto,'/', inverso)
