import pygame
from constants import *


def main():

    GAME_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Superman's Asteroids")
    
    while GAME_SCREEN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   return
        GAME_SCREEN.fill(color="blue", rect=None, special_flags=0)
        pygame.display.flip()

	


if __name__ == "__main__":
    pygame.init()
    main()
