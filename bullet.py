import pygame
from screensettings import WIDTH, HEIGHT

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

BULLET_R = [
    pygame.image.load('Materials/Images/Bullets/bullet_r.png').convert_alpha()
]
BULLET_L = [
    pygame.image.load('Materials/Images/Bullets/bullet_l.png').convert_alpha()
]
