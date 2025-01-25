import pygame
import numpy as np
from pygame import Vector2

screen_size = Vector2(800,600)

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_caption('SandboxRealms Pre-Alpha 1.0.0')
        self.screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)
    
    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    self.running = False


if __name__== '__main__':
    Game().run()