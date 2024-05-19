import pygame
from sys import exit
pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
sky_surface = pygame.Surface((800,300))
#sky_surface.fill('Cyan')
sky_surface = pygame.image.load('background/Sky.png')
ground_surface = pygame.Surface((800,100))
snail_surface = pygame.image.load('characters/snail/snail1.png')
#ground_surface.fill('Brown')
ground_surface = pygame.image.load('background/ground.png')
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render("My game", False, 'Black')
snail1_x = 800
snail1_y = 270
while True:
    screen = pygame.display.set_mode((800, 400))
    screen.blit(ground_surface,(0,300))
    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(300,50))
    snail1_x = snail1_x - 1
    if(snail1_x < -100):
        snail1_x = 800
    screen.blit(snail_surface,(snail1_x, snail1_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)