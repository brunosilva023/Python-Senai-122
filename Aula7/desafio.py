ecommerce = {
'livro':25.15,
'tablet':3000.0,
'fone':500.0
}

carrinho = {
'produtos':[],
'valores':[]
}

produto1 = input('produto: ')
produto2 = input('produto: ')

carrinho['produtos'].append(produto1)
carrinho['produtos'].append(produto2)
carrinho['valores'].append(ecommerce[produto1])
carrinho['valores'].append(ecommerce[produto2])

formas_pagamentos =  {'pix','cc','cd'}
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('Digite a forma de pagamento: ')
print(carrinho)
soma =  sum(carrinho['valores'])
print('Total -  R$', soma)
print('Obrigada volte sempre! ')