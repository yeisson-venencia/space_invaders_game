from Component import Component
import pygame

class Player(Component):
    def __init__(self, image_path, pos_x, pos_y, speed_x, speed_y, screen: pygame.Surface):
        super().__init__(image_path, pos_x, pos_y, speed_x, speed_y, screen)
