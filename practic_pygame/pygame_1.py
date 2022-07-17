import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

background = rect(screen, (156, 156, 156), (0, 0, 500, 500))

body = circle(screen, (255, 255, 0), (250, 250), 150)
body_bound = circle(screen, (0, 0, 0), (250, 250), 150, 2)

left_eye = circle(screen, (255, 0, 0), (250-70, 250-40), 35)
left_pupil = circle(screen, (0, 0, 0), (250-70, 250-40), 15)
left_bound = circle(screen, (0, 0, 0), (250-70, 250-40), 35, 1)

right_eye = circle(screen, (255, 0, 0), (250+70, 250-40), 25)
right_pupil = circle(screen, (0, 0, 0), (250+70, 250-40), 12.5)
right_bound = circle(screen, (0, 0, 0), (250+70, 250-40), 25, 1)

mouth = rect(screen, (0, 0, 0), (250-80, 250+65, 160, 30))

left_brow = polygon(screen, (0, 0, 0), [(230, 200), (100, 120), (110, 110), (240, 190)])
right_brow = polygon(screen, (0, 0, 0), [(280, 195), (400, 165), (395, 150), (275, 180)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()