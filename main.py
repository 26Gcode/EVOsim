import pygame
import numpy as np

PARTICLE_NUMBER = 300
WIDTH = 1600
HEIGHT = 1000
NUM_TYPES = 3
COLOR_STEP = 360 // NUM_TYPES

def update_particles(positions, velocity, types):
    new_position = np.empty_like(positions) 
    new_velocity = np.empty_like(velocity)

    for i in range(PARTICLE_NUMBER):
        pos_x, pos_y = positions[i]
        particle_type = types[i]
        
        if particle_type == 0:
            new_position[i] = pos_x, pos_y
            new_velocity[i] = 0,0

    
    return new_position, new_velocity

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    
    pos = np.random.rand(PARTICLE_NUMBER, 2) * [WIDTH, HEIGHT]
    types = np.random.randint(0,NUM_TYPES,PARTICLE_NUMBER)
    velocity = np.random.rand(PARTICLE_NUMBER, 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill((0,0,0))

        update_particles(pos, velocity, types)

        new_pos, new_velocity, new_types = [], [], []
        
        for i in range(PARTICLE_NUMBER):
            color = pygame.Color(0, 0, 255)
            color.hsva = (types[i] * COLOR_STEP, 100,100,100)
            pygame.draw.circle(screen, color, (int(pos[i, 0]), int(pos[i, 1])), 2)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit    

if __name__== '__main__':
    main()
