'''DESAFIO 14:
Escreva um programa que converta graus celcius para graus fahrenheit'''

celcius = float(input('Qual a temperatura do ambiente em °C:')) # recebe um valor em Celcius
fahre = ((celcius * 9) / 5) + 32                                      # converte para fahrenheit

# resultado
print(f'A temperatura em °F é: {fahre:.2f}')
