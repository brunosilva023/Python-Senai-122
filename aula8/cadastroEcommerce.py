# cadastro no e-commerce

dados = {
'login':[],
'senha':[]
}

print('cadastre-se:')

cad_login = input('cadastre seu login: ')
cad_senha = input('cadastre a sua senha:')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)
      
# acessar o e-commerce
print('acesse a aplicação: ')
acesso_login = input("digite seu login para acessar: ")
acesso_senha = input("digite sua senha para acessar: ")

if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]:
    print('seja bem vindo (a) ao ecommerce z')
else:
    print('ditação de senha e login incorreta')
    print('faça novamente')

# verificar a lista de produtos
# comprar um produto
# paga o produto

