'''DESAFIO 62:
Melhore D61 perguntando para o usuario se ele quer mostra mais alguns termos. O programa 
encerrara quando ele disser que quer o termo.
'''

from time import sleep

inicia = True

while inicia == True:
    pt = int(input('Primeiro termo: '))
    r = int(input('Qual a razão:'))
    p = pt
    decimo = 0
    print(pt, end=' -> ')

    while decimo != 9:
        decimo += 1
        pa = p + r
        p = pa
        print(pa, end=' -> ')
    print('ACABOU')
    desliga = str(input('Deseja fazer outra PA: [S/N]')).strip().upper()

    if desliga[0] in 'S':
        inicia = True

    elif desliga[0] in 'N':
        inicia = False

    else:
        while True:
            desliga = str(input('Resposta invalida. tente novamente: [S/N]')).strip().upper()
            if desliga[0] in 'S':
                inicia = True
                break
              
            elif desliga[0] in 'N':
                inicia = False
                break

print('FINALIZANDO')
sleep(2)
print('ATE A PROXIMA!!')
