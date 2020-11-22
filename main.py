import pygame
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

# Title and icon
pygame.display.set_caption('Space Invadors')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 96, 128))
    pygame.display.update() 
