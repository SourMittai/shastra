# SHASTRA Physics Simulator
import pygame
import numpy

#Defining the Variables:

G = 6.67e-11
m1 = 1.99e30
m2 = 5.97e24
r = 1.496e11
v = 2.98e4

F = G*((m1*m2)/r**2)


real_a = F/m2



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
earth_pos = pygame.math.Vector2(earth_x, earth_y)
earth_vs = 0 #velocity towards star
earth_vo = v #orbital velocity
earth_a = real_a * scale_time ** 2


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    screen.fill((0, 0, 0))
    sun = pygame.draw.circle(screen,(255, 0, 0), sun_pos, 10)
    earth = pygame.draw.circle(screen, (173, 216, 230), earth_pos, 2)

    # Falling mechanic
    earth_vs = (earth_vs + earth_a) / scale_dist
    # distance = distance + earth_vs

    direction_sun = pygame.math.Vector2.normalize(sun_pos - earth_pos)
    earth_pos += direction_sun * earth_vs

    direction_tangent = direction_sun.rotate(90)
    earth_pos += direction_tangent * ((earth_vo * scale_time) / scale_dist)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    
##Scale = 200 px = 1.496e11 m