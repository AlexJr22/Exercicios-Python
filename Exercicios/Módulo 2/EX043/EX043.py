''' DESAFIO 43:
Desenvolva uma logica que leia o peso de uma pessoa, calcule seu IME e mostre seu status, de acordo com a tabela abaixo:
    -> abaixo de 18,5: abaixo do peso
    -> entre 18.5 e 25: peso ideal
    -> 25 até 30:sobrepeso
    -> acima de 30 obesidade
    -> acima de 40 obesidade mórbida
'''

# dados da pessoa
altura = float(input('Qual sua altura?: '))
peso = float(input('Qual seu peso?: '))
imc = peso / (altura * altura)

# resultado da pesquisa
print(f'Sei IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal!!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está OBESO!')
elif imc >= 40:
    print('Você está com OBESIDADE MORBIDA!!')
