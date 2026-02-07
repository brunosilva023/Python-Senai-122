print('Aula - 8')

print('1 Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.')
numero = int(input('Digite um numero:'))
if numero >0:
    print('o numero digitado foi :', numero, 'Então ele é positivo')
elif numero == 0:
    print('o numero digitado foi :', numero, 'Então ele é zero')
else:
    print('o numero digitado foi :', numero, 'Então ele é negativo')

print('\n2 Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.')
idade = int(input('Digite sua idade:'))
if idade >= 18:
    print('a idade informada foi :', idade, 'Apto a votar')
else:
    print('a idade informada foi :', idade, 'não está apto a votar')

print('\n3 Declara uma variável com um número qualquer, determine se um número é par ou ímpar.')
numero = int(input('Digite um numero:'))
resto = numero % 2 
if resto==0:
    print('o numero informado  foi :', numero, 'então ele é par')
else:
    print('o numero informado  foi :', numero, 'então ele é impar')


print('\n4 Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno')
medida1 = int(input('Digite a primeira medida:'))
medida2 = int(input('Digite a segunda medida:'))
medida3 = int(input('Digite a terceira medida:'))

if medida1== medida2==medida3:
    print('é um triangulo equilatero, pois todos os lados possuem a mesma medida.')
if medida1 == medida2 or medida3:
    print('é um triangulo isósceles, pois dois lados possuem a mesma medida ')
else:
    print('é um triangulo escaleno, pois todos os lados possuem medidas diferentes')

print('\n5 Determine se um número é múltiplo de 5 e 7.')



print('\n6 Verifique se um número é positivo e maior que 10')



print('\n7 Verifique se um número é divisível por 3 ou 5.')

