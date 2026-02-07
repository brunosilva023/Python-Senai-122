'jokempo'
print( 'Pedra Papel Tesoura')
import random
lista_maquina = ['','🪨','🧻','✂️']
chute_maquina = random.choice(lista_maquina)
chute_jogador = ['','🪨','🧻','✂️']
print(('Digite seu objeto: '))
print('1🪨,|2🧻,|3-✂️')
meu_chute = int(input('escolha pelo indice: '))
print('a maquina escolheu',chute_maquina)
print(' o jogador escolheu', meu_chute)
#🪨🧻✂️
