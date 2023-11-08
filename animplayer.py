import pygame
from screensettings import WIDTH, HEIGHT

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

RUN_RIGHT = [pygame.image.load(fr'Materials/Images/Anim/run_r/{i}.png').convert_alpha() for i in range(1, 9)]
RUN_LEFT = [pygame.image.load(fr'Materials/Images/Anim/run_l/{i}.png').convert_alpha() for i in range(1, 9)]
IDLE = [pygame.image.load(fr'Materials/Images/Anim/idle/{i}.png').convert_alpha() for i in range(1, 7)]
