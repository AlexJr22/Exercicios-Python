'''DESAFIO 11:
Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e mostre a quantidade de tinta necessaria pra pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².'''

altura = int(input('Altura da parede: '))   # recebe a altura da parede
largura = int(input('Largura da parede: ')) # recebe a largura da parede
metro = largura*altura                      # calcula a área da parede
area_tinta = metro/2                        # calcula a área da tinta

# resultado
print(f'A parede tem {metro}m² e serão necessarios {area_tinta} litros de tinta pra pintala')
