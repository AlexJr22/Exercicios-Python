''' DESAFIO 4:
Crei um script em Python que leia algo pelo teclado e mostre seu tipo primitivo'''

txt = input('Digite Algo:')     # variavel que recebe um valor pelo teclado

print('O tipo primitivo dessse valor é:', type(txt))# mostra o tipo primitivo
print('Só tem espaço?', txt.isspace())              # mostra se só a espaços 
print('É um número?', txt.isnumeric())              # mostra se o valor é só um número
print('É alfabético?', txt.isalpha())               # mostra se o valor é alfabético(só contém letras)
print('É um alfanumérico?', txt.isalnum())          # mostra se o valor é alfanumérico(contém letras e números)
print('Está em maiúsculas?', txt.isupper())         # mostra se o valor só contém somente letras maiúsculas
print('Está em minúsculas', txt.islower())          # mostra se o valor só contém somente letras minúsculas
print('Está capitalizado?', txt.istitle())          # mostra se a primeira letra da String é maiúsculas
