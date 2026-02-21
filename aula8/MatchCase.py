# # ***EXERCÍCIOS com match/ case:*** 

print('1: Verificando se o número é par ou ímpar')
numero = int(input('numero : '))

match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('Impar')


print('2: Verificando se um número é positivo, negativo ou zero')
numero = int(input('numero : '))

match numero:
    case numero if numero == 0:
        print('Zero')
    case numero if numero < 0: 
        print('Negativo')
    case _:
        print('Positivo')


print('3: Verificando se uma string é vazia ou não')

string =input('Digite algo : ')

match string:
    case '':
        print('vazio')
    case _:
        print('preenchido')


print('4: Verificando se um número é maior, menor ou igual a 10')
numero = int(input('numero : '))

match numero:
    case numero if numero == 10:
        print('Dez')
    case numero if numero < 10: 
        print('Menor que dez')
    case _:
        print('Maior que dez')

print('5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)')

idade = int(input('idade : '))

match idade:
    case idade if idade <= 12:
        print('Criança')
    case idade if idade >= 13 and idade <=17:
        print('Adolescente')

    case idade if idade >= 18 and idade <=35:
            print('Jovem')
    case idade if idade >= 36 and idade <=64:
            print('Adulto')
    case _:
        print('idoso')


print( ' Fim ')