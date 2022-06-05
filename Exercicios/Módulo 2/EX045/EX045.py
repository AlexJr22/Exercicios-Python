''' DESAFIO 45:
Crie um programa que faça o computador joga jokenpo com você
'''

from random import choice

itens = ('pedra', 'papel', 'tesoura')
computador = choice(itens)  # a maquina escolha um item aleatorio dentro da tupla

user_name = str(input('Qual o nome do Jogador: '))

# escolha do jogador
print(f'''\033[;35m{user_name} escolha uma das alternativas abaixo:\033[m
\033[;33m
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura
\033[m''')

user_choice = int(input('Qual sua escolha: ')) # escolha do jogador

# logica do jogo

print(f'O computador escolheu: {computador}')
print()
if computador == 'pedra':
    if user_choice == 1:
        print('EMPATE')
    elif user_choice == 2:
        print(f'O jogador {user_name} venceu!!!')
    elif user_choice == 3:
        print('O computador venceu!!1')
    elif user_choice >= 4:
        print('\033[;31mopção invalida\033[m')
elif computador == 'papel':
    if user_choice == 1:
        print('O computador venceu!!!')
    if user_choice == 2:
        print('EMPATE')
    if user_choice == 3:
        print(f'O jogador {user_name} venceu!!!')
    elif user_choice >= 4:
        print('\033[;31mopção invalida\033[m')
elif computador == 'tesoura':
    if user_choice == 1:
        print(f'O jogador {user_name} venceu!!!')
    if user_choice == 2:
        print('O computador venceu!!!')
    if user_choice == 3:
        print('EMPATE')
    elif user_choice >= 4:
        print('\033[;31mopção invalida\033[m')
