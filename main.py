import pygame
pygame.init()

window_size = window_width, window_height = 800, 600

screen = pygame.display.set_mode(window_size)

# Background
background_color = (0, 19, 26)

# Title and icon
pygame.display.set_caption('Space Invadors')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('space-ship.png')
player_image_with = player_image.get_width()
player_image_height = player_image.get_height()

player_position_x = (window_width - player_image_with) // 2
player_position_y = int(window_height*0.9) - player_image_height

def player():
    screen.blit(player_image,(player_position_x,player_position_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_color)
    player()
    pygame.display.update() 
