import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw (self, screen):
        center = tuple(map(int, self.position))
        radius = int(self.radius)
        pygame.draw.circle(screen, "white", center, radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt