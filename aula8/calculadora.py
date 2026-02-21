def soma():
    n1  = float(input('n1: '))
    n2  = float(input('n2: '))
    print('= ', n1+n2)


def sub():
    n1  = float(input('n1: '))
    n2  = float(input('n2: '))
    print('=', n1-n2)


def mult():
    n1  = float(input('n1: '))
    n2  = float(input('n2: '))
    print('= ', n1*n2)


def divi():
    n1  = float(input('n1: '))
    n2  = float(input('n2: '))
    print('=', n1/n2)

def calculadora():
    operacao = input('''
            escolha a operação: 
                     +
                     -
                     /
                     *    
                    ''')
    if operacao == '+':
       soma()
    elif operacao == '-':
       sub()
    elif operacao == '/':
        divi()
    elif operacao == '*':
        mult()
    else:
        print('Digite algo valido: ')                               



def loop():
    while True:
        calculadora()


loop()