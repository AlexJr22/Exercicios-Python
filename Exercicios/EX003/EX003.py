'''Crie um script em Python que leia dos números e mostre no terminal a soma entre ele'''

num1 = int(input('Digite um número: '))     # variavel que recebe o primeiro número
num2 = int(input('Digite outro número: '))  # variavel que recebe o segundo número

# somando os valores diretos na função print()

print(f'\033[34mA soma entre os valores é {num1 + num2}\033[m!')

# somando os valores dentro de outra variavel

soma = num1 + num2

print(f'\033[33mA soma entre os valores é {soma}!\033[m')
