import pygame
import numpy
from pygame import Vector2
import random

screen_size = Vector2(800,600)

class Particle:
    def __init__(self, size, color, position):
        self.size = size
        self.color = color
        self.position = Vector2(position)
        
class ParticleManager:
    def __init__(self):
        self.particles = []

    def update(self):
        test = 1

    def add(self, particles):
        self.particles.extend(particles)


    def draw(self):
        test = 2


class Sim:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock() 

        self.pm = ParticleManager()

        self.screen = pygame.display.set_caption('EVOsim')
        self.screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)
    
    def update(self):
        self.pm.add([Particle((random.randinit(1,3), random.choice(['red', 'blue', 'green']), random.randit(0, screen_size.x), -10))])

    def draw(self, surface):
        surface.fill('black')
        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    self.running = False
            

            self.draw(self.screen)


if __name__== '__main__':
    Sim().run()

