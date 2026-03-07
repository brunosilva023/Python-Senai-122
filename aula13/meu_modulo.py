# crie um número aleatório de 5,10

import random


def atividade_1(n1,n2):
   return random.randint(n1, n2)



# 2 - Crie 3 números aleatórios

def atividade_2(n1,n2):
   return random.randint(n1,n2)


# 3 - Crie um número aleatório entre 10 a 30 utilize o range()

def atividade_3():
   n = random.randrange(10,30)
   return n


# 4 - Contagem regressiva simples Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)   

def atividade_4():
    for i in range(10, 0, -1):
        print(i)
        
    print("Fogo!")
