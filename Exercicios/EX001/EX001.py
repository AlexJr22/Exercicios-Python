'''Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vinda 
de acordo com o valor digitado'''

nome = str(input('Qual seu nome?: '))           # variavel q recebe o nome do usuario

print(f'Seja bem-vindo \033[33m{nome}\033[m!')  # print que mostra a mensagem de boas-vindas
