import pygame
import random
import sys

pygame.init()
pygame.mixer.init () 

LARGURA = 800
ALTURA = 400





tela = pygame.display.set_mode([LARGURA,ALTURA])
pygame.display.set_caption('JOGO DE OBSTACULOS')

# variáveis do jogo
# carregamento das imagens
theme = pygame.mixer.music.load('assets/m.mp3')
pulo_m = pygame.mixer.music.load('assets/m2.mp3')
trex1 = pygame.image.load('assets/m1.png')
trex2 = pygame.image.load('assets/m2.png')
trex3 = pygame.image.load('assets/m3.png')
ob1 = pygame.image.load('assets/ob2.png')
ob2 = pygame.image.load('assets/ob2.png')
chao = pygame.image.load('assets/g1.png')

# carregou  a img


im = 60,60

imagem_menor = pygame.transform.scale(trex1, im)
imagem_menor2 = pygame.transform.scale(trex2, im)
imagem_menor3 = pygame.transform.scale(trex3, im)

trex_x = 100
trex_y = 200

# pulo
vel_y = 0
gravidade = 1
pulando = False

# posicionamento do chão
chao_x = 0

# posicionamentos dos cactos
cact_x = 800
cact_y = 300

# frame 
frame  = 0

# texto na tela 
pontuacao = 0
fonte = pygame.font.SysFont('arial', 30)
game_over  = False

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        # x  = pygame.mixer.Sound("")
        # pygame.mixer.music.load("sounds/startup.mp3")
        pygame.mixer.music.play()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            sound = pygame.mixer.Sound('assets/m2.mp3')
            sound.play()
            if event.key == pygame.K_SPACE and not pulando:
                vel_y = -18
                
                pulando = True  

            if event.key == pygame.K_r and game_over:
                trex_y = 300
                cact_x = 800
                pontuacao = 0
                game_over = False

    if not game_over:
        vel_y += gravidade
        trex_y += vel_y
        if trex_y >= 300:
           trex_y = 300
           pulando = False  
        chao_x  -= 8
        if chao_x <= -800:
           chao_x = 0
        cact_x -= 8
        if cact_x < 0:
            cact_x = random.randint(800,1000)
            pontuacao += 1
        frame += 1
        if frame > 20:
            frame = 0
        if frame <  10:
            trex = imagem_menor
        elif frame >=  10 and frame <=15 :
            trex = imagem_menor2
        else:
            trex = imagem_menor3       

        # colisao 
        trex_rect = trex.get_rect(topleft=(trex_x, trex_y)) 
        cacto_rect = ob1.get_rect(topleft=(cact_x, cact_y))

        if trex_rect.colliderect(cacto_rect):
            game_over = True
    tela.fill(('yellow'))

    tela.blit(chao, (chao_x, 340))
    tela.blit(chao, (chao_x +800, 340))

    tela.blit(trex, (trex_x, trex_y))


    tela.blit(ob1, (cact_x, cact_y))

    # pontuação
    texto = fonte.render('SCORE: '+ str(pontuacao), True, (0,0,0))
    tela.blit(texto, (650,20))

    if game_over:
        texto2 = fonte.render('GAME OVER - clique em R para voltar', True, (255,0,0))
        tela.blit(texto2, (150,150) )
    pygame.display.update()

    clock.tick(30)    





