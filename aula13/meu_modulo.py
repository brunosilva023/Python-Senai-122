# # crie um número aleatório de 5,10

import random


def atividade_1(n1,n2):
   return random.randint(n1, n2)


# # 2 - Crie 3 números aleatórios

def atividade_2(n1,n2):
   return random.randint(n1,n2)


# # 3 - Crie um número aleatório entre 10 a 30 utilize o range()

def atividade_3():
   n = random.randrange(10,30)
   return n


# # 4 - Contagem regressiva simples Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)   

def atividade_4():
    for i in range(10, 0, -1):
        print(i)
        
    print("Fogo!")

# 5 - Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

def atividade_5():
# Peça ao usuário que insira um número inteiro 
    numero = int(input("Digite um número inteiro positivo: "))
    try:
        if numero < 2:
            print("Informe um número par, maior que dois")
        else:
            soma_pares = 0
    # faça o loop com range e for até o numero positivo 
            for i in range(2, numero + 1, 2):
    # calcule a soma de todos os números pares de 2 até o número inserido.
                soma_pares += i
            print(f"A soma dos pares de 2 até {numero} é: {soma_pares}")
    except:
        print("Por favor, insira um número inteiro válido.")

#6 - Tabuada de multiplicação

def atividade_6():
    numero1 = int(input("Digite um número inteiro positivo: "))
    try:
        if numero1 <0:
            print("Informe um número maior que zero")
        else:         
                for i in range(1,11):
                    print( numero1 ,"x",i, '=', numero1*i)
    except:
        print("informar um numero valido")


#7 -  Números ímpares reversos
def atividade_7():
    for i in range(99,0,-2):
        print(i)
