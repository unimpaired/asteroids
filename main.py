import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard


def main():
    pygame.init()
    pygame.display.set_caption("Superman's Asteroids")
    GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    scoreboard = Scoreboard(GAME_SCREEN, SCOREBOARD_FONT_SIZE, SCOREBOARD_FONT_COLOR )
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("You have lost")
                pygame.EXIT
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    scoreboard.increase(10)
                    asteroid.split()
                
        GAME_SCREEN.fill(BLACK)
        for obj in drawable:
            obj.draw(GAME_SCREEN)
        
        scoreboard.draw()
        pygame.display.flip()
        


if __name__ == "__main__":
    main()