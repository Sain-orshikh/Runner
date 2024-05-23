import pygame
from sys import exit
from random import randint

def player_animation():
    global player_surface, player_index
    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if (player_index >= len(player_walk)):
            player_index = 0
        player_surface = player_walk[int(player_index)]
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = round(current_time/1000)
    score_surface = test_font.render(f'Score: {score}',False,(64,64,64))
    score_rectangle = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rectangle)
    return score
def display_end_score():
    end_score = score
    end_score_surface = test_font.render(f'Score: {end_score}',False,'White')
    end_score_rectangle = end_score_surface.get_rect(center = (100,100))
    screen.blit(end_score_surface,end_score_rectangle)
def display_tries():
    tries_surface = test_font.render(f'Tries: {tries}',False,'White')
    tries_rectangle = tries_surface.get_rect(center = (100,150))
    screen.blit(tries_surface, tries_rectangle)
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -=4
            if (obstacle_rectangle.bottom == 300):
                screen.blit(snail_surface, obstacle_rectangle)
            if (obstacle_rectangle.bottom == 210):
                screen.blit(fly_surface, obstacle_rectangle)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []
def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return True
    else: return False


pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = True
screen = pygame.display.set_mode((800, 400))
screen_rectangle = screen.get_rect(topleft = (800,400))
start_time = 0
tries = 1
score = 0

sky_surface = pygame.Surface((800,300))
#sky_surface.fill('Cyan')
sky_surface = pygame.image.load('background/Sky.png').convert()

#ground_surface.fill('Brown')
ground_surface = pygame.Surface((800,100))
ground_surface = pygame.image.load('background/ground.png').convert()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
#box_color = #c0e8ec

#obstacle
obstacle_rectangle_list=[] 
snail_crawl_1 = pygame.image.load('characters/snail/snail1.png').convert_alpha()
snail_crawl_2 = pygame.image.load('characters/snail/snail2.png').convert_alpha()
snail_crawl = [snail_crawl_1, snail_crawl_2]
snail_index = 0
snail_surface = snail_crawl_1
snail_rectangle = snail_surface.get_rect(midbottom = (0,0))

fly_flight_1 = pygame.image.load('characters/fly/fly1.png').convert_alpha()
fly_flight_2 = pygame.image.load('characters/fly/fly2.png').convert_alpha()
fly_flight = [fly_flight_1, fly_flight_2]
fly_index = 0
fly_surface = fly_flight_1
fly_rectangle = fly_surface.get_rect(midbottom = (0,0))

player_stand = pygame.image.load('characters/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rectangle = player_stand.get_rect(center = (400,200))
player_walk_1 = pygame.image.load('characters/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('characters/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surface = player_walk[player_index]
player_jump = pygame.image.load('characters/player/jump.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
pmpf = 5

restart_surface = test_font.render("RESTART", False, 'Gold')
restart_rectangle = restart_surface.get_rect(center = (400, 50))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

frame_rate = 60
while True:

    snail_rectangle = snail_surface.get_rect(midbottom = (randint(900,1100),300))
    fly_rectangle = fly_surface.get_rect(midbottom = (randint(900,1100),210))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE and player_rectangle.bottom >= 300):
                    player_gravity = -20
            if event.type == pygame.MOUSEMOTION:
                if (player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300):
                    player_gravity = -20
        else:
            if event.type == pygame.MOUSEMOTION:
                    if (restart_rectangle.collidepoint(event.pos)):
                        game_active = True
                        tries +=1
            start_time = pygame.time.get_ticks()
        if game_active:    
            if event.type == obstacle_timer:
                if (randint(0,2) % 2 == 0):
                    obstacle_rectangle_list.append(snail_rectangle)
                else:
                    obstacle_rectangle_list.append(fly_rectangle)
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surface = snail_crawl[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surface = fly_flight[fly_index]
            
    pygame.display.update()
    clock.tick(frame_rate)

    if game_active:
        player_animation()
        screen.blit(ground_surface,(0,300))
        screen.blit(sky_surface,(0,0))
        screen.blit(player_surface,player_rectangle)
        screen.blit(snail_surface,snail_rectangle)

        score = display_score()
        
        player_rectangle.left +=pmpf
        player_gravity +=1
        player_rectangle.y +=player_gravity
        if player_rectangle.bottom > 300:
            player_rectangle.bottom = 300

        if player_rectangle.y == 300:
            player_rectangle.y == 300   

        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)
        
        if(player_rectangle.left >= 800):
            player_rectangle.right = 0
        
        player_collision = collision(player_rectangle, obstacle_rectangle_list)
        if(player_collision == True):
            game_active = False
            pmpf = 0
            obstacle_rectangle_list.clear()
            end_time = pygame.time.get_ticks() - start_time
        #collision yes = True, collision no = False
        #mouse_position = pygame.mouse.get_pos()
        #if (player_rectangle.collidepoint(mouse_position)):
            #print(pygame.mouse.get_pressed())
        
        #key = pygame.key.get_pressed()
        #if key[pygame.K_SPACE]:
            #player_rectangle.center +=10 
    else:
        screen.fill('Black')
        screen.blit(player_stand, player_stand_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        snail_rectangle = snail_surface.get_rect(midbottom = (800,300))
        player_rectangle = player_surface.get_rect(midbottom = (80,300))
        pmpf = 5
        restart_time = pygame.time.get_ticks()
        start_time = start_time - restart_time
        display_end_score()
        display_tries()