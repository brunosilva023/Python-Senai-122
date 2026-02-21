# cadastro no e-commerce

dados = {
    'login':[],
    'senha':[],
        'produtos':{
                '1' : ['computador Dell', 5000.0],
                '2' : ['fone apple',2000.0],
                '3' : ['mouse lenovo',250.0],
                '4' : ['monitor lenovo',3000.0]
            }
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


# verificar a lista de produtos
    print('produtos')

    produto = input(f'''
    {dados['produtos']} - escolha 1 - 2 - 3 - 4
    ''')

# comprar um produto
    carrinho = []
    valores = []
    carrinho.append(dados['produtos'][produto][0])
    valores.append(dados['produtos'][produto][1])
    print(carrinho[0],valores[0])

# paga o produto

    soma = sum(valores)
    print('valor a pagar - R$: ',soma)
    pag = input('digite a forma de pagamento : ')
    print('forma de pagamento : ',pag)
    print('Obrigada e volte sempre !! ')

else:
    print('ditação de senha e login incorreta')
    print('faça novamente')