print('Aula - 8')

print('1 Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.')
numero = int(input('Digite um numero:'))
if numero >0:
    print('o numero digitado foi :', numero, 'Então ele é positivo')
elif numero == 0:
    print('o numero digitado foi :', numero, 'Então ele é zero')
else:
    print('o numero digitado foi :', numero, 'Então ele é negativo')

print('------'*20)

print('\n2 Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.')
idade = int(input('Digite sua idade:'))
if idade >= 18:
    print('a idade informada foi :', idade, 'Apto a votar')
else:
    print('a idade informada foi :', idade, 'não está apto a votar')

print('------'*20)

print('\n3 Declara uma variável com um número qualquer, determine se um número é par ou ímpar.')
numero = int(input('Digite um numero:'))
resto = numero % 2 
if resto==0:
    print('o numero informado  foi :', numero, 'então ele é par')
else:
    print('o numero informado  foi :', numero, 'então ele é impar')

print('------'*20)

print('\n4 Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno')
medida1 = int(input('Digite a primeira medida:'))
medida2 = int(input('Digite a segunda medida:'))
medida3 = int(input('Digite a terceira medida:'))

if medida1== medida2==medida3==medida1:
    print('é um triangulo equilatero, pois todos os lados possuem a mesma medida.')
if medida1 != medida2 !=medida1 != medida3 !=medida2 != medida1 !=medida2 != medida3!=medida3 != medida2 !=medida3 != medida1:
    print('é um triangulo isosceles, pois possuem as medidas diferentes ')
else:
    print('é um triangulo escaleno, pois todos os lados possuem duas medidas diferentes')

print('------'*20)

print('\n5 Determine se um número é múltiplo de 5 e 7.')
numero = int(input('Digite um numero:'))
resto5 = numero%5
resto7 = numero%7

if resto5==0:
    print('o numero informado  foi :', numero, 'então ele é é multiplo de 5')
elif resto7==0:
    print('o numero informado  foi :', numero, 'então ele é é multiplo de 7')
else:
    print('o numero informado  foi :', numero, 'então ele não é multiplo de 5 e 7')

print('------'*20)

print('\n6 Verifique se um número é positivo e maior que 10')
numero = int(input('Digite um numero:'))
if numero >=0 and numero>10:
    print('o numero digitado foi :', numero, 'Então ele é positivo e maior que 10')
elif numero>=0 and numero<=10:
    print('o numero digitado foi :', numero, 'Então ele é  positivo,maior que zero e menor ou igual que 10')
else: 
    print('o numero digitado foi :', numero, 'Então ele é negativo')

print('------'*20)

print('\n7 Verifique se um número é divisível por 3 ou 5.')
numero = int(input('Digite um numero:'))
resto3 = numero%3
resto5 = numero%5

if resto3==0:
    print('o numero informado  foi :', numero, 'então ele é é divisivel de 3')
elif resto5==0:
    print('o numero informado  foi :', numero, 'então ele é é divisivel de 5')
else:
    print('o numero informado  foi :', numero, 'então ele não é divisivel de 3 e 5')

print('------'*20)
print('exercicios finalizados com sucesso !')
