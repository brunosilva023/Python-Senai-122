# 1

msg = 'Seja bem vindos'
print(msg)

# 2

verdadeiro = True
tipo  =  type(verdadeiro)
print(tipo)

# 3

n1 = 1.2
n2 =  52.0
resultado =  n1 * n2
print(resultado)


# 4 

n1 = 5
n2 = 52
resultado =  n1 - n2
print(resultado)

# 5

n2 = 10
n3 = 20
resultado_2 = n2 / n3
print(resultado)



# 6

n4 =  5
n5 = 10

resultado_3 = n4 // n5
print(resultado_3)


# 7 

x = 1.
y = 2.5
z = 5.4
w = 15.8

print(x* y* z*w)

# 8

numero =  10
dobro = numero ** 2
print(dobro)

# 9 


print('SISTEMA DE CADASTRO')

nome  =  input('Nome: ')
idade  =  int(input('idade: '))
cidade  =  input('Cidade: ')
graduacao = input('Graduação:')
estado_civil = input('Estado Civil: ')

print(f'''
DADOS INSERIDOS NO SISTEMA:
      
            NOME:{nome}
            IDADE:{idade}
            CIDADE:{cidade}
            GRADUAÇÃO:{graduacao}
            ESTADO CIVIL:{estado_civil}     
''')

