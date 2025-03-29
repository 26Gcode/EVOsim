import pygame
import numpy as np

PARTICLE_NUMBER = 200
WIDTH = 1600 
HEIGHT = 1000
NUM_TYPES = 3
COLOR_STEP = 360 // NUM_TYPES
K = 0.05
RED_EAT_MINIMUM = 2
BLUE_EAT_MINIMUM = 3

FORCES = np.array([
    [-5,  0,  10], 
    [0,   0,   0],  
    [-5,  10,   -5],    
])

MIN_DISTANCES = np.array([
    [10, 0, 20],
    [0, 0, 0],
    [10, 20, 10],  
])
RADII = np.array([
    [75, 0, 75],
    [0, 0, 0],
    [75, 75, 75],  
])

eat_counts = np.zeros(PARTICLE_NUMBER,dtype=int)

def update_particles(positions, velocity, types, eat_counts):
    new_position = np.empty_like(positions)
    new_velocity = np.empty_like(velocity)

    for i in range(PARTICLE_NUMBER):
        total_force_x, total_force_y = 0.0, 0.0
        pos_x, pos_y = positions[i]
        vel_x, vel_y = velocity[i]
        p_type = types[i]

        if p_type == 1:
            new_position[i] = pos_x, pos_y
            new_velocity[i] = 0, 0
            continue

        for j in range(PARTICLE_NUMBER):
            if i != j:
                dir_x = positions[j, 0] - pos_x
                dir_y = positions[j, 1] - pos_y

                dis = np.sqrt(dir_x**2 + dir_y**2)
                if dis > 0:
                    dir_x, dir_y = dir_x / dis, dir_y / dis 
                    other_type = types[j]

                    if dis < MIN_DISTANCES[p_type, other_type]:
                        force = abs(FORCES[p_type, other_type]) * -3 * (1 - dis / MIN_DISTANCES[p_type, other_type]) * K
                        total_force_x += dir_x * force
                        total_force_y += dir_y * force

                    if dis < RADII[p_type, other_type]:
                        force = FORCES[p_type, other_type] * (1 - dis / RADII[p_type, other_type]) * K
                        total_force_x += dir_x * force
                        total_force_y += dir_y * force

                    if dis <= 4:
                        if p_type == 0 and other_type == 3:
                                eat_counts[i] += 1
                                types[j] = -1
                        
                        if p_type == 3 and other_type == 2:
                                eat_counts[i] += 1
                                types[j] = -1
                        
        new_vel_x = vel_x + total_force_x
        new_vel_y = vel_y + total_force_y
        new_pos_x = (pos_x + new_vel_x) % WIDTH
        new_pos_y = (pos_y + new_vel_y) % HEIGHT

        new_position[i] = new_pos_x, new_pos_y
        new_velocity[i] = new_vel_x, new_vel_y

    return new_position, new_velocity, types, eat_counts

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    pos = np.random.rand(PARTICLE_NUMBER, 2) * [WIDTH, HEIGHT]
    types = np.random.randint(0, NUM_TYPES, PARTICLE_NUMBER)
    velocity = np.zeros((PARTICLE_NUMBER, 2))
    global eat_counts
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))

        pos, velocity, types, eat_counts = update_particles(pos, velocity, types, eat_counts)

        new_positions, new_velocities, new_types = [], [], []
        for i in range(PARTICLE_NUMBER):
            if types[i] != -1: 
                new_positions.append(pos[i])
                new_velocities.append(velocity[i])
                new_types.append(types[i])
            
                if types[i] == 0 and eat_counts[i] >= RED_EAT_MINIMUM:
                    new_positions.append(pos[i] + np.random.uniform(-5,5,size=2))
                    new_velocities.append(velocity[i])
                    new_types.append(types[i])

        pos = np.array(new_positions)
        velocity = np.array(new_velocities)
        
        for i in range(PARTICLE_NUMBER):
            color = pygame.Color(0, 0, 255)
            color.hsva = (types[i] * COLOR_STEP, 100,100,100)
            pygame.draw.circle(screen, color, (int(pos[i, 0]), int(pos[i, 1])), 2)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()