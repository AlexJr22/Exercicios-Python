''' Desafio 65:
Crie um programa que leia varios números inteiros pelo teclado. No final mostre a média entre 
todos os valores e qual foi o maior e o menor valor digitado.
O programa dever perguntar ao usuario se ele quer continuar a digitar.
'''


Nunbers = cont = maior = menor = 0 

while True:

  num = int(input('Digite um número: '))
  Nunbers += num
  cont += 1

  if cont == 1:
    maior = menor = num
    
  else:
    if maior < num:
      maior = num
    if menor > num:
      menor = num
    
  endProgram = str(input('Adicionar outro número?: ')).upper().strip()
  if endProgram[0] in 'SN':
    if endProgram[0] == 'N':
      break

  if endProgram[0] not in 'SN':
      endProgram = str(input('[ERRO] resposta invalida, Adicionar outro número?: ')).upper().strip()

      if endProgram[0] in 'SN':
        if endProgram[0] == 'N':
          break

print('-=' * 15)
print(f'A média e dos valores digitados é: {Nunbers/cont}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
print('-=' * 15)
