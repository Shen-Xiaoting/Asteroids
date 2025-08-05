import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Field = AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in list(asteroids):
            for shot in list(shots):
                if shot.colliding(asteroid):
                    asteroid.split()
                    shot.kill()
           


        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()
