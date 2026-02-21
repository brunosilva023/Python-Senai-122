# palavra reservada condicao
# loop finito
import time 


# iterando percorrendo 
# repetições 


l =  [1,2,3,4]


for i in range(10):
    produto = input('Digite o id do produto') 
    if i == 5:
        break

    # for   -  sim
# while - sim


dados = {
'produtos' : []
}


# for produto in range(5):
#     prod =  input('Digite o nome de um produto: ')
#     dados['produtos'].append(prod)
# print(dados)



# for dado in dados.values():
#     print(dado)



perg =  input('Deseja comprar? sim ou não ')


while perg == 'sim':
    prod = input('nome do produto: ')
    dados['produtos'].append(prod)
    
    print(dados)
    perg =  input('Deseja continuar? sim ou não ')
else:
    print('Obrigado volte sempre! ')


