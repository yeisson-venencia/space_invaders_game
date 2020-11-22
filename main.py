import pygame
from random import randint
pygame.init()

window_size = window_width, window_height = 800, 600

screen = pygame.display.set_mode(window_size)

# Background
background_color = (0, 19, 26)
background_image = pygame.image.load('background.png')


# Title and icon
pygame.display.set_caption('Space Invadors')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('player.png')
player_image_with = player_image.get_width()
player_image_height = player_image.get_height()

player_position_x = (window_width - player_image_with) // 2
player_position_y = int(window_height*0.9) - player_image_height
player_left_pace = 0
player_right_pace = 0
player_speed = 5

# Monster
monster_image = pygame.image.load('enemy.png')
monster_image_with = monster_image.get_width()
monster_image_height = monster_image.get_height()

monster_position_x = randint(0,window_width-monster_image_with)
monster_position_y = randint(0,3) * monster_image_height
monster_left_pace = 0
monster_right_pace = 0
monster_x_speed = 2
monster_y_speed = monster_image_height

# Bounderies
left_limit = window_width*0
right_limit =  window_width*1 - player_image_with

def player(x_position, y_position):
    screen.blit(player_image,(x_position,y_position))

def monster(x_position, y_position):
    screen.blit(monster_image,(x_position,y_position))

running = True
while running:
    screen.fill(background_color)
    screen.blit(background_image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_left_pace = player_speed
            elif event.key == pygame.K_RIGHT:
                player_right_pace = player_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_left_pace = 0
            elif event.key == pygame.K_RIGHT:
                player_right_pace = 0

    #monster movement
    monster_position_x += monster_x_speed
    if monster_position_x < left_limit or monster_position_x > right_limit:
        monster_x_speed *= -1
        monster_position_y += monster_y_speed

    # Execute player movement
    player_position_x += player_right_pace - player_left_pace
    # Check Bounderies
    if player_position_x < left_limit:
        player_position_x = left_limit
    elif player_position_x > right_limit:
        player_position_x = right_limit 
    player(player_position_x,player_position_y)
    monster(monster_position_x,monster_position_y)
    pygame.display.update() 
