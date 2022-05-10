'''DESAFIO 15:
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por KM rodado'''

alug_dia = int(input('Quantos dias o carro foi alugado?: ')) # recebo a quantidade de dias alugados
KM_rodado = int(input('Quantos KM foram rodados durante o período de aluguel?: ')) # recebe quantos km foram percorridos

valor_alug = 60 * alug_dia  # calcula o valor do aluguel
valor_km = 0.15 * KM_rodado # calcula o valor dos KM percorridos

# resultado
print('-='*17)
print('\033[33m|',f'DIAS ALUGADOS: {valor_alug}'.center(30),'|')
print('|',f'KM RODADOS: {valor_km:.2f}'.center(30),'|')
print('|',f'VALOR TOTAL: {valor_alug+valor_km}'.center(30),'|\033[m')
print('=-'*17)
