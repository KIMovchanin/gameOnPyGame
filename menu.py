import pygame
import nameinput
import howtoplay as htp
from screensettings import WIDTH, HEIGHT


def startmenu():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH*0.88916, HEIGHT))
    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 70)
    menu_label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 40)

    name_game = label.render('Survivor', False, (27, 168, 83))

    start_game = menu_label.render('Start', False, 'White')
    start_game_rect = start_game.get_rect(topleft=(WIDTH*0.416, HEIGHT*0.5))

    how_to_play_game = menu_label.render('How to play?', False, 'White')
    how_to_play_game_rect = how_to_play_game.get_rect(topleft=(WIDTH*0.3583, HEIGHT*0.66))

    goodbye_game = menu_label.render('Quit', False, 'White')
    goodbye_game_rect = goodbye_game.get_rect(topleft=(WIDTH*0.42083, HEIGHT*0.83))

    bg = pygame.image.load('Materials/Images/back_menu.jpg')

    running = True
    while running:
        pygame.display.update()

        screen.blit(bg, (0, 0))
        screen.blit(name_game, (WIDTH*0.3416, HEIGHT*0.0083))
        screen.blit(start_game, start_game_rect)
        screen.blit(how_to_play_game, how_to_play_game_rect)
        screen.blit(goodbye_game, goodbye_game_rect)

        mouse = pygame.mouse.get_pos()

        if start_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            nameinput.entername()
            break
        elif how_to_play_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            htp.howtoplay()  # запускает инструкцию с тем как играть
            break
        elif goodbye_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
