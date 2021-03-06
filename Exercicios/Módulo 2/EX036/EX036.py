'''DESAFIO 36:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pergunta 
o valor da casa e o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do valor do salário ou então o emprestimo será negado.
'''

print('-=-'*15)
print('            EMPRESTIMO BANCARIO')
print('-=-'*15)

# dados bancarios
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o valor do seu salário: '))
anos = int(input('Em quantos anos você vai pagar o emprestimo: '))
prestaçao = anos * 12
v_mensal = casa / prestaçao

salario_2 = salario * 0.30    # 30% DO SALÁRIO DO USUARIO

# dados pro usuario
print('-=-'*15)
print(f'O valor das parcelas não podem axceder 30%(R${salario_2:.2f}) do seu salario')
print(f'O valor do seu salário é R${salario:.2f}')
print(f'O número de meses para completar o pagamento é {prestaçao}')
print(f'O valor das parcelas é R${v_mensal:.2f}')
print('-=-'*15)

# aprovação do emprestimo
if v_mensal > salario_2:
    print('Seu emprestimo foi negado')
else:
    print('Seu emprestimo foi aprovado')
    print(f'Você pagará {prestaçao} parcelas de R${v_mensal:.2f}')
