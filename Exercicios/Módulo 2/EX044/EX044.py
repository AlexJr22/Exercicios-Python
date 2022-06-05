''' DESAFIO 44:
Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
    -> à vista dinheiro/cheque: 10% de desconto
    -> à vista no cartão:5% de descoto
    -> em ate duas vezes no cartão: preço normal
    -> 3x o mais no cartão: 20% juros
'''

# preço do produto
preco = float(input('Qual o preço do produto: '))

# forma de pagamento
print('''Escolha uma forma de pagamento abaixo: 
[ 1 ] á vista no dinheiro/cheque: 10% de desconto
[ 2 ] á vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Digite o número da opção escolhida: '))

# resultado
print()
if opcao == 1:
    novopreco = preco - (preco * 0.10)
    print(f'O preço final do produto é R${novopreco:.2f}')
elif opcao == 2:
    novopreco = preco - (preco * 0.05)
    print(f'O preço final do produto é R${novopreco:.2f}')
elif opcao == 3:
    novopreco = preco
    print(f'O preço final do produto é R${novopreco:.2f}')
elif opcao == 4:
    novopreco = preco + (preco * 0.20)
    print(f'O preço final do produto é R${novopreco:.2f}')
