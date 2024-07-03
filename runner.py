import pygame
import math
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
def display_wins():
    wins_surface = test_font.render(f'Wins: {wins}',False,'White')
    wins_rectangle = wins_surface.get_rect(center = (100,200))
    screen.blit(wins_surface,wins_rectangle)
def display_victory_end_score():
    end_score = score
    end_score_surface = test_font.render(f'Score: {end_score}',False,'White')
    victory_end_score_surface = pygame.transform.scale_by(end_score_surface,1.25)
    victory_end_score_rectangle = end_score_surface.get_rect(center = (100,125))
    screen.blit(victory_end_score_surface,victory_end_score_rectangle)
def display_victory_tries():
    tries_surface = test_font.render(f'Tries: {tries}',False,'White')
    victory_tries_surface = pygame.transform.scale_by(tries_surface,1.25)
    victory_tries_rectangle = tries_surface.get_rect(center = (100,200))
    screen.blit(victory_tries_surface, victory_tries_rectangle)
def display_victory_wins():
    wins_surface = test_font.render(f'Wins: {wins}',False,'White')
    victory_wins_surface = pygame.transform.scale_by(wins_surface,1.25)  
    victory_wins_rectangle = wins_surface.get_rect(center = (100,275))
    screen.blit(victory_wins_surface,victory_wins_rectangle)
def display_victory():
    victory_surface = test_font.render('Victory!',False,'Gold')
    victory_surface = pygame.transform.scale_by(victory_surface,2)
    victory_rectangle = victory_surface.get_rect(center = (150,50))
    screen.blit(victory_surface,victory_rectangle)
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -=8
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
def victory():
    print('victory')
    return True
def victory_animation():
    screen.blit(sky_surface,sky_rectangle)
    screen.blit(ground_surface,ground_rectangle)
    screen.blit(spaceship_surface,spaceship_rectangle)
    spaceship_rectangle.y -=5
    

pygame.init()
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = True
screen = pygame.display.set_mode((800, 400))
screen_rectangle = screen.get_rect(topleft = (800,400))
start_time = 0
tries = 1
score = 0
wins = 0
wins_add = True
spawn_obstacle = True
active = 0
paused = 1
won = 2
game_state = active

music = pygame.mixer.Sound('audio/music.mp3')
music.set_volume(0.5)
play_music = True
background_x = 0
scroll = 0

#double_jump_animation_bool = False
#double_jump_animation = pygame.image.load('characters/spaceship.png').convert_alpha()
#double_jump = True

sky_surface = pygame.Surface((800,300))
sky_surface = pygame.image.load('background/Sky.png').convert()
sky_surface_width = sky_surface.get_width()
sky_rectangle = sky_surface.get_rect()

ground_surface = pygame.Surface((800,100))
ground_surface = pygame.image.load('background/ground.png').convert()
ground_surface_width = ground_surface.get_width()
ground_rectangle = ground_surface.get_rect()

galaxy_surface = pygame.Surface((800,400))
galaxy_surface = pygame.image.load('background/galaxy.png').convert()

tiles = math.ceil(screen_rectangle.width  / sky_surface_width) + 1

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

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

#spaceship
spaceship_surface = pygame.image.load('characters/spaceship/spaceship2.png').convert_alpha()
spaceship_surface = pygame.transform.scale_by(spaceship_surface, 2)
victory_spaceship_surface = pygame.transform.scale_by(spaceship_surface, 4)
victory_spaceship_rectangle = victory_spaceship_surface.get_rect(bottomleft = (250,300))
spaceship_rectangle = spaceship_surface.get_rect(center=(3000,300))
spaceship_scroll = 0
smpf = 5
spaceship_spawn_score = randint(75,125)
#player
player_stand = pygame.image.load('characters/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rectangle = player_stand.get_rect(center = (400,200))
player_walk_1 = pygame.image.load('characters/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('characters/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surface = player_walk[player_index]
player_jump = pygame.image.load('characters/player/jump.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (160,300))
player_jump_sound = pygame.mixer.Sound('audio/jump.mp3')
player_jump_sound.set_volume(0.3)
player_gravity = 0
pmpf = 0

#restart
restart_surface = test_font.render("RESTART", False, 'Gold')
restart_rectangle = restart_surface.get_rect(center = (400, 50))
victory_restart_surface = pygame.transform.scale_by(restart_surface,1.5)
victory_restart_rectangle = victory_restart_surface.get_rect()

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
        if (game_state == active):
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE and player_rectangle.bottom >= 300):
                    player_gravity = -20
                    player_jump_sound.play()
                #if (event.key == pygame.K_SPACE and player_rectangle.bottom < 300 and double_jump == True):
                    #double_jump_animation_bool = True
                    #player_gravity = -15
                    #double_jump = False
            #if event.type == pygame.MOUSEMOTION:
                #if (player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300):
                    #player_gravity = -20
        elif (game_state == paused):
            if event.type == pygame.MOUSEMOTION:
                    if (restart_rectangle.collidepoint(event.pos)):
                        game_state = active
                        tries +=1
                        wins_add = True
                        spaceship_scroll = 0
                        smpf = 5
                        play_music = True
                        spaceship_spawn_score = randint(75,125)
            start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    game_state = active
                    tries +=1
                    wins_add = True
                    spaceship_scroll = 0
                    smpf = 5
                    play_music = True
                    spaceship_spawn_score = randint(75,125)
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN):
                    game_state = active
                    tries +=1
                    wins_add = True
                    spaceship_scroll = 0
                    smpf = 5
                    play_music = True
                    spaceship_spawn_score = randint(75,125)
        else:
            if event.type == pygame.MOUSEMOTION:
                    if (restart_rectangle.collidepoint(event.pos)):
                        game_state = active
                        tries +=1
                        wins_add = True
                        spaceship_scroll = 0
                        smpf = 5
                        play_music = True
                        spaceship_spawn_score = randint(75,125)
            start_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    game_state = active
                    tries +=1
                    wins_add = True
                    spaceship_scroll = 0
                    smpf = 5
                    play_music = True
                    spaceship_spawn_score = randint(75,125)
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN):
                    game_state = active
                    tries +=1
                    wins_add = True
                    spaceship_scroll = 0
                    smpf = 5
                    play_music = True
                    spaceship_spawn_score = randint(75,125)
        if (game_state == active):    
            if event.type == obstacle_timer:
                if (randint(0,2) % 2 == 0):
                    if(spawn_obstacle==True):
                        obstacle_rectangle_list.append(snail_rectangle)
                else:
                    if(spawn_obstacle==True):
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

    if (game_state == active):
        #game_state = won
        spawn_obstacle = True
        player_animation()
        restart_rectangle.center = (3000,300)
        #screen.blit(ground_surface,(0,300))
        #screen.blit(sky_surface,(0,0))
        #screen.blit(player_surface,player_rectangle)
        #screen.blit(snail_surface,snail_rectangle)

          #draw scrolling background
        for i in range(0, tiles):
            screen.blit(sky_surface, (i * sky_surface_width + scroll, 0))
            sky_rectangle.x = i * sky_surface_width + scroll
            #pygame.draw.rect(screen, (255, 0, 0), sky_rectangle, 1)
        for i in range(0, tiles):
            screen.blit(ground_surface, (i * ground_surface_width + scroll, 300))
            ground_rectangle.x = i * ground_surface_width + scroll
            #pygame.draw.rect(screen, (255, 0, 0), ground_rectangle, 1)
        screen.blit(player_surface,player_rectangle)
        #screen.blit(snail_surface,snail_rectangle)
        if(score>=spaceship_spawn_score):
            screen.blit(spaceship_surface,spaceship_rectangle)
            spaceship_rectangle.y = 80
            spaceship_rectangle.x = 800 - spaceship_scroll
            spaceship_scroll +=smpf
            spawn_obstacle = False
        #scroll background

        #reset scroll
        if abs(scroll) > sky_surface_width:
            scroll = 0
        if abs(scroll) > ground_surface_width:
            scroll = 0
        #if (double_jump_animation_bool == True):
            #screen.blit(double_jump_animation,player_rectangle)
            #double_jump_animation_bool = False
        scroll -=5

        score = display_score()
        
        player_rectangle.left +=pmpf
        player_gravity +=1
        player_rectangle.y +=player_gravity
        if player_rectangle.bottom > 300:
            player_rectangle.bottom = 300

        #double_jump = True
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list)
        
        if(player_rectangle.left >= 800):
            player_rectangle.right = 0
        
        player_collision = collision(player_rectangle, obstacle_rectangle_list)
        if(player_collision == True):
            game_state = paused
            pmpf = 0
            obstacle_rectangle_list.clear()
            end_time = pygame.time.get_ticks() - start_time
            if play_music:
                play_music = False
                music.play()
            play_music = True
        #collision yes = True, collision no = False
        #mouse_position = pygame.mouse.get_pos()
        #if (player_rectangle.collidepoint(mouse_position)):
            #print(pygame.mouse.get_pressed())
        
        #key = pygame.key.get_pressed()
        #if key[pygame.K_SPACE]:
            #player_rectangle.center +=10
        if(player_rectangle.colliderect(spaceship_rectangle)):
            wins_bool=victory()
            if wins_bool and wins_add:
                wins_add = False
                wins +=1
            smpf = 0
            game_state = won
            if play_music:
                play_music = False
                music.play()
            play_music = True
    elif (game_state == paused):
        restart_rectangle.x = 335
        restart_rectangle.y = 50
        screen.fill('Black')
        screen.blit(player_stand, player_stand_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        snail_rectangle = snail_surface.get_rect(midbottom = (800,300))
        player_rectangle = player_surface.get_rect(midbottom = (80,300))
        pmpf = 0
        restart_time = pygame.time.get_ticks()
        start_time = start_time - restart_time
        display_end_score()
        display_tries()
        display_wins()
    elif (game_state == won):
        victory_restart_rectangle.x = 35
        victory_restart_rectangle.y = 325
        if (spaceship_rectangle.bottom > 30):
            screen.blit(ground_surface,(0,300))
            screen.blit(sky_surface,(0,0))
            screen.blit(spaceship_surface,spaceship_rectangle)
            spaceship_rectangle.y -=5
        if (spaceship_rectangle.bottom <= 30):
            if play_music:
                play_music = False
                music.play()
            screen.blit(galaxy_surface,(0,0))
            screen.blit(victory_spaceship_surface,victory_spaceship_rectangle)
            screen.blit(victory_restart_surface,victory_restart_rectangle)
            snail_rectangle = snail_surface.get_rect(midbottom = (800,300))
            player_rectangle = player_surface.get_rect(midbottom = (80,300))
            pmpf = 0
            restart_time = pygame.time.get_ticks()
            start_time = start_time - restart_time
            display_victory()
            display_victory_end_score()
            display_victory_tries()
            display_victory_wins()

