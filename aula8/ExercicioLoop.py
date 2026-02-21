# print('1 - Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000')

# c = 0
# while c < 1001:
#     print(c)
#     c  =  c  + 1



# print('2 - Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela')

# nomes = []
# pessoa = 1

# while pessoa <= 10:
#     nome = input(f"Digite o nome da pessoa {pessoa}: ")
#     nomes.append(nome)
#     pessoa += 1

# print("--- Nomes Cadastrados ---")
# for nome in nomes:
#     print(nome)
# print('cadastro realizado')




print('3 - Crie um sistema de notas alunos, com as seguintes operações:Utilize While ou for')

print('Sistema de notas de alunos')


# - Acesso a conta com condicionais
dados = {
    'login':[],
    'senha':[],
    'notas':[],
}

print('realize seu cadastro')
print ()
login = input('cadastre seu login: ')
senha = input('cadastre a sua senha:')
dados['login'].append(login)
dados['senha'].append(senha)


# - 3 chances de acessar o sistema

p = input('acesse ao sistema: sim ou não ?')
while  p == 'sim':

    for chances in range(3):
        alogin = input("digite seu login para acessar: ")
        asenha = input("digite sua senha para acessar: ")

        if alogin == dados['login'][0] and asenha == dados['senha'][0]:
            print('Sistema de notas')
            print()
            print("Informe as respectivas notas")
            print()
            nome= input("Digite o nome do aluno: ")
            print()
            nota1= int(input("Informe a primeira nota : "))
            nota2= int(input("Informe a segunda nota : "))
            nota3= int(input("Informe a terceira nota : "))
            print()
            media = (nota1+nota2+nota3)/3
            print()
            print(' a média do aluno : ',nome , 'é' ,media)
            while media>=7:
                print("Aprovado")
                break
            while media >=5:
                 print('Recuperação')
                 break
            else:
                 print('reprovado')
                 break
            print()
            print()
        print("obrigado")
    else:
            print('ditação de senha e login incorreta')
            print('conta bloqueada')
            
else: print("obrigado")
