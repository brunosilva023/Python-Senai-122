import pygame

pygame.init()
tamanho = 300,150  
screen = pygame.display.set_mode(tamanho)

run = True
while run:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False
        screen.fill('lightskyblue')
        pygame.draw.rect(screen,'black',(125,50,50,50))
        pygame.draw.line(screen,'green', (50, 50), (100, 50), 5)
        pygame.draw.ellipse(screen,'blue', (150, 100, 80, 40))
        pygame.draw.circle(screen, 'red', (30, 40), 20)
        pygame.display.update()

pygame.quit()
