import pygame
from sys import exit
pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400))

sky_surface = pygame.Surface((800,300))
#sky_surface.fill('Cyan')
sky_surface = pygame.image.load('background/Sky.png').convert()

#ground_surface.fill('Brown')
ground_surface = pygame.Surface((800,100))
ground_surface = pygame.image.load('background/ground.png').convert()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render("My game", False, 'Black')

snail_surface = pygame.image.load('characters/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (800,300))

player_surface = pygame.image.load('characters/player/player_walk_1.png')
player_rectangle = player_surface.get_rect(midbottom = (80,300))

frame_rate = 60
while True:
    screen.blit(ground_surface,(0,300))
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(300,50))
    screen.blit(player_surface,player_rectangle)
    screen.blit(snail_surface,snail_rectangle)
    
    player_rectangle.left +=1
    snail_rectangle.left -=1
    if(snail_rectangle.right <= 0):
        snail_rectangle.left = 800
    
    if(player_rectangle.colliderect(snail_rectangle) == True):
        player_collision = True
    else:
        player_collision = False
    #collision yes = True, collision no = False
    #mouse_position = pygame.mouse.get_pos()
    #if (player_rectangle.collidepoint(mouse_position)):
        #print(pygame.mouse.get_pressed())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rectangle.collidepoint(event.pos):
                #print('collision')
    pygame.display.update()
    clock.tick(frame_rate)