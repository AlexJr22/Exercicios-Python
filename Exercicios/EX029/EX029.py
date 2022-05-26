'''DESAFIO 29:
Escreva um programa que leia a velocidade de um carro.
Se a velocidade ultrapassar 80KM/h, mostre uma mensagem dizendo que o motorista foi multado.
    - A multa vai custar R$7,00 pro KM acima do limite'''

veloc = int(input('Qual a velocidade do veículo: '))    # recebe a velociade do veículo

if veloc > 80:
    multa = (veloc - 80) * 7                            # calcula a multa
    print('Você foi multado!!')
    print(f'A multa aplicada foi de R${multa}.')
else:
    print('Este veiculo não esta ultrapassando o limite de velocidade permitido!')
