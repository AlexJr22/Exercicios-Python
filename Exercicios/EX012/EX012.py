'''DESAFIO 12:
Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto'''

preco1 = float(input('Preço atual do produto: '))   # recebe um preço inicial do produto
novopreco = preco1 - preco1 * 5/100                 # calcula o desconto 5%

# resultado
print(f'O novo preço do produto é R${novopreco:.2f}')
