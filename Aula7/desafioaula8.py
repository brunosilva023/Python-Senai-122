# estruturas dados 
# listas tuplas conjuntos dicts  var 


dados = {
    'quartos':{
            'Simples': 100.00, 
            'Duplo': 150.00, 
            'Luxo': 250.00, 
             }
}


dados['nomes'] = [input('cliente: '),input('cliente: '), input('cliente: ') ]
dados['idade'] = [input('idade: '),input('idade:'), input('idade:')]


print(' quartos disponiveis: ')
print(dados['quartos'])


print('Escolha o quarto do cliente',dados['nomes'][0])
quarto = input('escolha o quarto: ')
quant_d = int(input('dias: '))
cal = dados['quartos'] [quarto ]* quant_d
print('Valor pago pelo cliente', dados['nomes'][0] ,'R$', cal)



print('Escolha o quarto do cliente',dados['nomes'][1])
quarto = input('escolha o quarto: ')
quant_d = int(input('dias: '))
cal = dados['quartos'][quarto ] * quant_d
print('Valor pago pelo cliente', dados['nomes'][1] ,'R$', cal)



print('Escolha o quarto do cliente',dados['nomes'][2])
quarto = input('escolha o quarto: ')
quant_d = int(input('dias: '))
cal = dados['quartos'][quarto ] * quant_d
print('Valor pago pelo cliente', dados['nomes'][2] ,'R$', cal)

# print(dados)
