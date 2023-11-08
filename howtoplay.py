import pygame
import menu
from screensettings import WIDTH, HEIGHT


def howtoplay():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH*0.88916, HEIGHT))

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 20)

    text_label1 = label.render('You need to survive 30 seconds and you will win, but you have only 7 bullets.', False,
                               'White')
    text_label2 = label.render('Kill 1 zombie = +100 points.', False, 'White')
    text_label3 = label.render('Survive 1 second = +10 points.', False, 'White')

    move_label = label.render('For move use arrows (<- and ->).', False, 'White')

    jump_label = label.render('For jump use space.', False, 'White')

    shoot_label = label.render('For shooting use key "f".', False, 'White')

    back_button = label.render('<- Back to menu.', False, 'Red')
    back_button_rect = back_button.get_rect(topleft=(WIDTH*0.025, HEIGHT*0.916))

    running = True
    while running:
        pygame.display.update()

        screen.blit(text_label1, (WIDTH*0.16, HEIGHT*0.33))
        screen.blit(text_label2, (WIDTH*0.36, HEIGHT*0.375))
        screen.blit(text_label3, (WIDTH*0.34583, HEIGHT*0.416))

        screen.blit(move_label, (WIDTH*0.325, HEIGHT*0.66))
        screen.blit(jump_label, (WIDTH*0.375, HEIGHT*0.7083))
        screen.blit(shoot_label, (WIDTH*0.3583, HEIGHT*0.75))
        screen.blit(back_button, back_button_rect)

        mouse = pygame.mouse.get_pos()
        if back_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu.startmenu()
            pygame.quit()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False
                pygame.quit()
                break

    pygame.quit()
