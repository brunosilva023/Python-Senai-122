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

