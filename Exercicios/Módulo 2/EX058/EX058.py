''' DESAFIO 58:
Melhore o jogo do Desafio 28 onde ocomputador vai pensa em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acerta, mostrando no final quantos palpites foram necessarios para vencer.
'''

from random import randint


computador = randint(1, 10) # escolhendo um número

print('\033[33mO computador pensou em um número entro 1 e 10!!\033[m')
user_choice = int(input("Adivinhe o número que o computador pensou: "))

# validando os dados

contador = 0 # contador de tentativas

while user_choice != computador:
    user_choice = int(input("você errou, tente novamente: "))
    contador += 1

print('O computador escolheu o número {}.'.format(computador))

if contador == 1:
    print('Parabens você acertou de primeira!!!')

elif contador <= 3:
    print('Você acertou com poucas tentativas!! PARABENS')
    print('Você tentou {}x'.format(contador))

elif contador >= 4:
    print('Você finalmente acerto!')
    print('Você tentou {}x'.format(contador))
    