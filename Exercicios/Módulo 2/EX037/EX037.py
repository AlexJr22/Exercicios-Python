'''DESAFIO 37:
Escreva um programa que leia um número interio qualquer e peça para o usuario escolher qual será a base 
de conversão:
    -> 1 para binária
    -> 2 para octal
    -> 3 para hexadecimal
'''

# ESCOLHA DO USUÁIO
num = int(input('Digite um número:'))   # recebe um número pelo teclado
print('''Escolha uma das bases númericas para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opçao = int(input('Qual sua opção: '))  # recebe a opção do usuário

# OPÇÕES DO USUÁRIO
if opçao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num)[:2]))
else:
    print('opção invalida, tente novamente!')
