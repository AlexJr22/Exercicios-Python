'''Faça uma script que leia um número inteiro pelo teclado e mostra seu sucessor e seu antecessor'''

num = int(input('Digite um número: ')) # recebe um valor pelo teclado

# calculando o resultado usando variaveis
ant = num - 1
suc = num + 1
print(f'O antecessor de {num} é {ant}!')
print(f'O sucessor de {num} é {suc}!')

# calculando o resultado direto na função print()
print(f'O antecessor de {num} é {num-1}!')
print(f'O sucessor de {num} é {num-1}!')
