import pygame
from pygame.locals import *
import random
import sys, os
import pickle

WIDTH = 1400
HEIGHT = 740
FPS = 12

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
class Game(object):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Guess the movie")
        self.clock = pygame.time.Clock()
        
        def desc(surf, text, x, y):
            font = pygame.font.Font('arial', 14)
            text_surface = font.render(text, True, 14)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface, text_rect)

    def play(self):
        while True:
            self.on_loop()
            self.on_render()

    def on_loop(self):    
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def on_render(self):
        pygame.display.update()
        self.clock.tick(FPS)  


if __name__ == "__main__":
    game = Game()
    game.play()