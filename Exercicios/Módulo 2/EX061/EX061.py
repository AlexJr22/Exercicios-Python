''' DESAFIO 61:
Refaça o D51, lendo o primeiro termo de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while.
'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão:'))
decimo = ta1 = 0
p = primeiro

print(primeiro, end=' -> ')

while decimo != 9:
    decimo += 1
    ta = p + razao
    p = ta
    print(ta, end=' -> ')
    
print('ACABOU')