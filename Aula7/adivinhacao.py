import random
aleatorio = random.randint(1,10)
chute = int(input('chute um numero: '))

if aleatorio == chute:
    print('acertei em cheio')
    print(' o numero é ', aleatorio)
else:
    print('Errou feio !')
    print('O numero é', aleatorio)
