import random
import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position.x, position.y, radius)
        self.velocity = velocity
    
    def draw (self, screen):
        center = tuple(map(int, self.position))
        radius = int(self.radius)
        pygame.draw.circle(screen, "white", center, radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_angle_pos = self.velocity.rotate(random_angle)
            new_angle_neg = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position, new_radius, new_angle_pos * 1.2)
            new_asteroid2 = Asteroid(self.position, new_radius, new_angle_neg * 1.2)
        