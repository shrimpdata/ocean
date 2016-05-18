import pygame

class Sprite(pygame.sprite.DirtySprite):
    pass

class MovingSprite(Sprite):

    def __init__(self):
        super().__init__()
        self.x_velocity = 0
        self.y_velocity = 0

    def set_x_velocity(self, velocity):
        self.x_velocity = velocity

    def set_y_velocity(self, velocity):
        self.y_velocity = velocity
