import pygame
from screensettings import WIDTH, HEIGHT

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT))

ZOMBIE_WALK_L = [
    pygame.image.load('Materials/Images/Anim/zombie_walk_l/1.png').convert_alpha()
]
