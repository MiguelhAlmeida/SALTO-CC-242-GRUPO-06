from random import randint

computador = randint(0, 5) #Faz o computador escolher um numero entre 0 e 5
print('Adivinhe o nùmero de 0 a 5')
#print('O número correto é: n{}'.format(computador))   *pra testar se o computador escolheu um número
acertou = False
while not acertou:
    jogador = int(input('Em que numero eu pensei?'))  # jogador escolher o numero

    if jogador == computador:
        print('Número correto!')
        acertou = True
    else:
        print('Número errado! Tente novamente.')