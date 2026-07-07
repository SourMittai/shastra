# SHASTRA Physics Simulator
import pygame
import numpy

#Defining the Variables:

G = 6.67e-11
m1 = 1.99e30
m2 = 5.97e24
v = 2.94e4




pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

px_dist = 300 #Setting distance on screen for 1 AU
time_real = 2629746

scale_dist = 1.496e11 / px_dist #Setting number of px per 1 AU
scale_time = time_real / 60 #Setting number of real world seconds per program second.

#Positions of the objects:
sun_x = 400
earth_x = sun_x + px_dist
earth_y = 300
sun_pos = pygame.math.Vector2(sun_x, 300)
real_sun_pos = pygame.math.Vector2(0, 0)
earth_pos = pygame.math.Vector2(earth_x, earth_y)
earth_start_dist = 1.49e11
real_earth_pos = pygame.math.Vector2(earth_start_dist, 0)
earth_velocity = pygame.math.Vector2(0, v)
distance_vector = real_sun_pos - real_earth_pos
r = distance_vector.length()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    screen.fill((0, 0, 0))

    sun_screen_pos = (real_sun_pos / scale_dist) + sun_pos

    sun = pygame.draw.circle(screen,(255, 0, 0), sun_screen_pos, 10)
    earth = pygame.draw.circle(screen, (173, 216, 230), earth_pos, 1)

    # Falling mechanic
    distance_vector = real_sun_pos - real_earth_pos
    r = distance_vector.length()
    F = G*((m1*m2)/r**2)
    real_a = F/m2
    direction_sun = pygame.math.Vector2.normalize(distance_vector)
    gravity_a = real_a * direction_sun
    earth_velocity += gravity_a * scale_time
    real_earth_pos += earth_velocity * scale_time
    earth_pos = (real_earth_pos / scale_dist) + sun_pos

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

