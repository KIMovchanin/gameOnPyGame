import pygame
import game
import menu
import topfive
from screensettings import WIDTH, HEIGHT


def win():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 40)
    win_label = label.render('You win!', False, 'LightGreen')
    win_label_rect = win_label.get_rect(topleft=(WIDTH*0.416, HEIGHT*0.16))

    play_again_label = label.render('Play again?', False, 'Red', 'DarkGreen')
    play_again_label_rect = play_again_label.get_rect(topleft=(WIDTH*0.38, HEIGHT*0.5))

    menu_label = label.render('Go to menu', False, 'White', 'DarkGreen')
    menu_label_rect = menu_label.get_rect(topleft=(WIDTH*0.33, HEIGHT*0.83))

    top_label = label.render('Top 5 players', False, 'White', 'DarkGreen')
    top_label_rect = top_label.get_rect(topleft=(WIDTH*0.66, HEIGHT*0.66))

    quit_label = label.render('Quit', False, 'White', 'DarkGreen')
    quit_label_rect = quit_label.get_rect(topleft=(WIDTH*0.5416, HEIGHT*0.83))

    running = True
    while running:
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        screen.blit(win_label, win_label_rect)
        screen.blit(play_again_label, play_again_label_rect)
        screen.blit(menu_label, menu_label_rect)
        screen.blit(top_label, top_label_rect)
        screen.blit(quit_label, quit_label_rect)

        if play_again_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game.play()
            break
        elif menu_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            menu.startmenu()
            break
        elif top_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            topfive.topfive()
            break
        elif quit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            break

        for event in pygame.event.get():  # за счёт метода pygame.event.get() мы получаем список из всех возможных
            # событий
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False
                pygame.quit()
                pygame.mixer.quit()
                break
    pygame.quit()
