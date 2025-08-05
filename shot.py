import pygame
from constants import *
from asteroid import *
from circleshape import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__ (x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw (self, screen):
        center = tuple(map(int, self.position))
        radius = int(SHOT_RADIUS)
        pygame.draw.circle(screen, "white", center, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt