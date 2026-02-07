#Exercício 0: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
texto='Exercicio 0'
print(texto)
numeros = list(range(2,22,2))
print(numeros)

# Exercício 1: Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.
texto='Exercicio 1'
print(texto)
numeros =[1,2,3,4,5,6]
print((numeros))


# Exercício 2: Acesse e imprima o terceiro elemento da lista `numeros`.
texto='Exercicio2'
print(texto)
print(numeros[2])



# Exercício 3: Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
texto='Exercicio3'
print(texto)
numeros.append(9)
print(numeros)

# Exercício 4: Remova o número 5 da lista `numeros` e imprima a lista resultante.
texto='Exercicio4'
print(texto)
del numeros[4]
print(numeros)

# Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.
texto='Exercicio5'
print(texto)
carros  =  ['ferrari', 'hb20', 'fusca']
print(carros+numeros)

# # Exercício 6: Use um loop `for` para percorrer e 
# # imprimir todos 
# # os elementos da lista  = [12,45,45,89,78,3,6,78,87]

# lista  =  [12,45,45,89,78,3,6,78,87]
# for n_lista in lista: 
#     print(n_lista)



# # Exercício 7: Verifique se o número 5 está 
# # presente na lista 
# # `numeros` e imprima uma mensagem informando 
# # se ele está na 
# # lista ou não.

##if 5 in numeros: 
   ##print('existe')
##else: 
   ##print('Não existe')     

##variavel  = 5
##for n in range(5,6):
    # x  =  int(input('Digite'))
    #if variavel in numeros:
      # print('certo')
   # else: 
    #   print('Não esta')     
#----------------------------------------
   
   
   
# 1

#lista  =  list(range(2,21,2))
#print(lista)

# 2

#numeros = [1,2,3,4,5,6,7,8,9,10]
#numeros =  list(range(1,11))


# 3

#numeros.append(9)


# 4

#numeros.remove(5)



# 5


#carros  =  ['tesla', 'ferrari','Jeep']
#print(carros,numeros)

#carros +=(numeros)

#print(carros)