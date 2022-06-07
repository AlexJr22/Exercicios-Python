''' DESAFIO 49:
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuario escolher, só que agora ultilizando um laço(for).
'''

user_num = int(input('Digite um número: ')) # recebe um número pelo teclado
print(f'tabuada de {user_num} é:')

for tabua in range(0, 11):                  # mostra a tabuada
    print(f'{user_num} * {tabua:02} = {user_num*tabua}')
