import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("OpenGL in Pygame")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    #
    # # Draw a simple triangle
    # glBegin(GL_TRIANGLES)
    # glColor3f(1, 0, 0)  # Red
    # glVertex3f(-0.5, -0.5, 0)
    # glColor3f(0, 1, 0)  # Green
    # glVertex3f(0.5, -0.5, 0)
    # glColor3f(0, 0, 1)  # Blue
    # glVertex3f(0, 0.5, 0)
    # glEnd()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()