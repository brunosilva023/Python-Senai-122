print("Exercícios com funções")
print("variáveis locais, globais e parâmetros")
print("''''"*10)


print("1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS. ")

numero = int(input("Informe o primeiro número :"))
numero2 = int(input("Informe o segundo número :"))

resto = numero % 2 
resto2 = numero2 % 2
if resto == 0:
    print("Par")
else:
    print("Ímpar")
if resto2 == 0:
    print("Par")
else:
    print("Ímpar")

print("2- CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS")

a = int(input("Informe o primeiro número :"))
b  = int(input("Informe o segundo número :"))
c = int(input("Informe o terceiro número :"))

def multiplicar_tres_numeros(a, b, c):
    return a * b * c

resultado = multiplicar_tres_numeros(a, b, c)
print(resultado) 

print("3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO")

base = int(input("Informe a base :"))
expoente = int(input("Informe o expoente :"))
def elevar_numero(base, expoente):
    return base ** expoente
resultado = elevar_numero(base,expoente)
print(resultado)



print("4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS")
idade = int(input("Informe a idade :"))

if idade >= 18:
        print("Acesso liberado: Você tem 18 anos ou mais.")
else:
        print("Acesso negado: Você é menor de idade.")

print("5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA")

ano_nascimento = int(input("Informe seu ano de nascimento :"))
ano_atual = int(input("Informe em que ano estamos :"))

def calcular_idade(ano_nascimento):
    return ano_atual - ano_nascimento
resultado = calcular_idade(ano_atual-ano_nascimento)
print(resultado)

maioridade = ano_atual-ano_nascimento
if maioridade >= 18:
        print("Maior de idade, você tem 18 anos ou mais.")
else:
        print("Você é menor de idade.")


print("6 - DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999")

ano = 1999
titulos = [1958, 1962, 1970, 1994, 2002]

if ano == 1999:
    print( "O Brasil não ganhou a copa")
else:
    print("O Brasil foi campeão nos anos " , titulos)


print("7 -DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE")
    

# 1 - Função - Cumprimentar o cliente
def cumprimentar_cliente():
    print("--" * 40)
    print("   Seja bem vindo !!  ")
    print("--" * 40)
    nome = input("Por favor, diga seu nome: ")
    print(f"Olá{nome}! É um prazer atendê-lo(a) hoje.")
    return nome

# 2 - Função - Restaurante (Cardápio e Pedidos)
def restaurante():
    cardapio = ["Salada","Macarronada","Sanduiche","Sorvete"]
    pedido = []
    for i, item in enumerate(cardapio, 1):

        print(f"{i} - {item}")
    print("0 - Finalizar Pedido")
    
    while True:
        try:
            opcao = int(input("\nEscolha o número do item que deseja (ou 0 para sair): "))
            
            if opcao == 0:
                break
            elif 1 <= opcao <= len(cardapio):
                item_escolhido = cardapio[opcao - 1]
                pedido.append(item_escolhido)
                print(f"-> {item_escolhido} adicionado ao pedido.")
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")
            
    return pedido

# 3 - Função principal para rodar o sistema
def main():
    cliente = cumprimentar_cliente()
    itens_pedidos = restaurante()
    
    print("\n" + "=" * 40)
    print(f"RESUMO DO PEDIDO DE: {cliente.upper()}")
    print("=" * 40)
    
    if not itens_pedidos:
        print("Nenhum item foi selecionado.")
    else:
        for item in itens_pedidos:
            print(f"- {item}")
        print("=" * 40)
        print("Agradecemos a preferência! Bom apetite!")

if __name__ == "__main__":
    main()