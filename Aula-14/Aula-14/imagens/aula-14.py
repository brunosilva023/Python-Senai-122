import pygame
import random
import sys


pygame.init()

L = 800
A = 400

tela = pygame.display.set_mode(L,A)
pygame.display.set_caption('TREX')


#variaveis do jogo
#carregar as imagens

trex1 = pygame.image.load('imagens/trex1.png')
trex2 = pygame.image.load('imagens/trex2.png')
trex3 = pygame.image.load('imagens/trex3.png')
ob1 = pygame.image.load('imagens/ob1.png')
ob2 = pygame.image.load('imagens/ob2.png')
chao = pygame.image.load('imagens/g1.png')




for event in pygame.event.get():
    if event.type == pygame.quit:
        pygame.quit()
        sys.exit()

"C:\Users\Aluno\Downloads\Aula-14\imagens"