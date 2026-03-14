import pygame
import random
import sys


pygame.init()
clock = pygame.time.Clock()
L = 800
A = 400

tela = pygame.display.set_mode([L,A])
pygame.display.set_caption('TREX')


#variaveis do jogo
#carregar as imagens

trex1 = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/trex1.png')
trex2 = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/trex2.png')
trex3 = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/trex3.png')
ob1 = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/ob1.png')
ob2 = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/ob2.png')
chao = pygame.image.load('C:/Users/Aluno/Downloads/Aula-14/imagens/g1.png')

im = 60,60

imagem_menor = pygame.transform.scale(trex1,(im))
imagem_menor2 = pygame.transform.scale(trex2,(im))
imagem_menor3 = pygame.transform.scale(trex3,(im))

trex_x = 100
trex_y = 200
#pulo

vel_y = 0
gravidade = 1
pulando = False

#posicionamento do chão
chao_x = 0

#posicionamento dos cactos
cact_x = 800
cact_y = 300

#frame

frame = 0

pontuacao = 0

fonte = pygame.font.SysFont('arial', 30)
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_SPACE and not pulando:
                vel_y = -18
                pulando = True

            if event.key == pygame.K_r and game_over:
                trex_y = 300
                cact_x = 800
                pontuacao = 0
                game_over = False
    if not game_over:
        vel_y+= gravidade
        trex_x += vel_y
        if  trex_y>=300:
            trex_y =300
            pulando = False
        chao_x -=5
        if chao_x <= -800:
            chao_x = 0
        cact_x =8
        if cact_x < 0:
            cact_x = random.randint(800,1000)
            pontuacao += 1
        frame =+ 1
        if frame>20:
            frame =0
        if frame<10:
            trex = imagem_menor

        elif frame >= 10 and frame <=15:
            trx = imagem_menor2
        else:
            trex = imagem_menor3

        #colisão
        trex_rect = trex.get_rect(topleft=(trex_x,trex_y))
        cacto_rect = ob1.get_rect(topleft=(cact_x,cact_y))

        if trex_rect.colliderect(cacto_rect):
            game_over = True
    tela.fill(255,255,255)    tela.blit(chao,(chao_x,340)40    tela.blit(chao,(chao_x+800,340))40    tela.blit(trex,(trex_x,trex_y)40
    tela.blit(ob1, (cact_x,cact_y))

    #pontuação
    texto = fonte.render('Score:', + str(pontuacao),true,(0,0,0))
    tela.blit(texto,(650,20))

    if game_over:
        texto2 = fonte.render('GAME OVER - clique em R para voltar',True(255,0,0))
        tela.blit(texto2,(350,150))
    pygame.display.update()

    clock.tick(30)