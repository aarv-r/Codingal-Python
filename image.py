import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("dog")
c =pygame.image.load("dog.jpg").convert_alpha()
c=pygame.transform.scale(c,(150,150))
while not False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,255,0))
    screen.blit(c,(350,0))
    pygame.display.flip()