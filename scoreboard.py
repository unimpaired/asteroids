import pygame
from constants import *

class Scoreboard:
    def __init__(self, screen, font, color):
        self.screen = screen
        self.font = pygame.font.Font(None, font)
        self.color = color
        self.score = 0
        self.position = (10, 10)
    
    def increase(self, score):
        self.score += score
        
    def reset(self, score):
        self.score = 0
        
    def draw(self):
        score_str = f"Current Score -  {self.score}"
        score_surface = self.font.render(score_str, True, self.color)
        self.screen.blit(score_surface, self.position)