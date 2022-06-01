'''DESAFIO 10:
Crie um programa que leia quanto dinheiro(em R$) uma pessoa tem na carteira e mostre quanto ela tem em dólares ela pode comprar (CONSIDERE US$1,00 = R$3,27)'''

real = float(input('Quantos R$ você possui: R$'))   # recebe valor em Reais
dolar = real/3.27                                   # variavel que converte reais para dólar

# resultado
print(f'Você possui R${real}')
print(f'Com essa quantia você pode compra ${dolar:.2f}')
