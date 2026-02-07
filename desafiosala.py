# atividade em sala

# variaveis  =  1 dado
# listas =  []
# tuplas  = ()
# conjuntos  =  {}
# dicionarios  =  {'key':'value'}


# e-commerce
# Produtos:  Livros, tablets e fones de ouvido
# As ações: 
# Comprar()
# Pagar()
# mostra o valor da compra


ecommerce = {
'livros':{
    'a':50.0,
    'b':150
},
'tablets':{
    'x': 150.,
    'y':250.55
},
'fones':{
    'tx':52.22,
    'ty':155.00
}
}


meus_produtos ={
'carrinho':[],
'valores':[]
}


secao1 = input('digite a secao: ')
prod1 = input('Produto 1')
secao2 = input('digite a secao: ')
prod2 = input('Produto 2')


meus_produtos['carrinho'].append(prod1)
meus_produtos['carrinho'].append(prod2)


meus_produtos['valores'].append(ecommerce[secao1][prod1])
meus_produtos['valores'].append(ecommerce[secao2][prod2])


print(meus_produtos)


total = sum(meus_produtos['valores'])


print('Total R$ - ', total)


lista_pag =  ['pix', 'cc', 'cd']
forma = input('digite a forma de pagamento: ')
print('forma de pagamento> ', forma)
print('Obrigada volte sempre! ')