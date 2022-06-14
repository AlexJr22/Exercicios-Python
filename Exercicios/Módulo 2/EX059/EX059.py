''' DESAFIO 59:
Crie um programa que leia dois valores e mostre na tela um menu:
    - 1 somar
    - 2 multiplicar
    - 3 maior
    - 4 novos números 
    - 5 sair do programa
Seu programa devará realizar a operação solicitada em cada caso.
'''

from time import sleep

# coletando os valores
print('Digite dois valores: ')
num1 = int(input('1º valor: '))
num2 = int(input('2º valor: '))

# validando as escolhas
opçao = 0
while opçao != 5:
    print('''    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] FINALIZAR PROGRAMA''')
    print('=' * 30)
    opçao = int(input('>>>>>>'))  # escolha do usuario

    if opçao == 1:  # SOMA
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))

    elif opçao == 2:  # MULTIPLICAÇÃO
        mult = num1 * num2
        print('A multiplicação entre {} x {} é {}'.format(num1, num2, mult))
        
    elif opçao == 3:  # MAIOR
        if num1 > num2:
            maior = num1
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))

        elif num2 > num1:
            maior = num2
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))

        elif num1 == num2:
            print('Os dois valores são inguais')

    elif opçao == 4:  # NOVO NÚMERO
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))

    elif opçao == 5: # FINALIZAR
        print('Finalizando o programa!!')

    else:
        print('Opção invalida!')
    print('=' * 30)
    sleep(1)
    