# def calcular():
#     try:
        
#         l = [1,2,3]
#         n1  =  10
#         n2  =  3
#         x  = 100
#         print(n1  / n2 + x)
#         print(l[n2])
        
#     except ValueError as erro:
#         print(erro)
#     except ZeroDivisionError as erro:
#         print(erro)
#     except TypeError as erro:
#         print(erro)
#     except NameError as erro:
#         print(erro)
#     except IndexError as erro :
#         print(erro)
#     else:
#         print('Não existe erro...')
        
#     finally:
#         print('Fim de carregamento...')

# ZerroDivisionError
# calcular()


# print("Exercicios !!")

# print("Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro. ")

# def calcular():
#     try:
#         n1= int(input("Informe um número: "))
#         print(n1)
#     except ValueError as erro:
#         print("número informado não é inteiro",erro)
# calcular()


# print("Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.")

# def calcular():
#     try:
#         n1= int(input("Informe um número: "))
#         n2= int(input("Informe um número: "))    
#         print(n1/n2)
#     except:
#         print("ZeroDivisionError")
# calcular()

# print("Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista")

# l = [0,1,2,3,4,5]
# indice = int(input("Informe o indice desejado:"))
# c=0
# resultado = l[indice]

# def calcular():
#     try:
#         for resultado in l:
#             print("o indice é ",l) 
#     except:
#         print("indice invalido")

# calcular()
