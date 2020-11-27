import pygame
from Position import Position

class Component(object):
    def __init__(self, image_path, pos_x, pos_y, speed_x, speed_y, screen: pygame.Surface):
        self.image = pygame.image.load(image_path)
        self.position = Position(pos_x,pos_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.screen = screen

        @property
        def image_width(self):
            return self.image.get_width()
        
        @property
        def image_height(Self):
            return self.image.get_height()

        def move_up(self):
            self.position.y -= self.speed_y
        
        def move_down(self):
            self.position.y += self.speed_y
        
        def move_left(self):
            self.position.x -= self.speed_x
        
        def move_right(self):
            self.position.x += self.speed_x
        
        def left_limit(self):
            return 0
        
        def right_limit(self):
            return self.screen.get_width() - self.image_width
        
        def top_limit(self):
            return 0 - self.image_height
        
        def bottom_limit(self):
            return self.screen.get_height()