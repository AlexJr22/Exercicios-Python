''' DESAFIO 31:
Desemvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de 200km, a R$0,45 para viagens mais longas'''

dist = float(input('Quantos KM tem a viagem?: '))   # recebe a distância da viagem

# calculando o preço da viagem
if dist >= 200:
    print(f'Você pagara nessa viagem R${dist * 0.45}')
else:
    print(f'Voce pagara nessa viagem R${dist * 0.50}')
