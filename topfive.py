import pygame
from bdconnect import top
from screensettings import WIDTH, HEIGHT


def topfive():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 30)
    try:
        top1 = label.render(f'1. {top[0][0]} - {top[0][1]}', False, 'White')
    except:
        pass
    try:
        top2 = label.render(f'2. {top[1][0]} - {top[1][1]}', False, 'White')
    except:
        pass
    try:
        top3 = label.render(f'3. {top[2][0]} - {top[2][1]}', False, 'White')
    except:
        pass
    try:
        top4 = label.render(f'4. {top[3][0]} - {top[3][1]}', False, 'White')
    except:
        pass
    try:
        top5 = label.render(f'5. {top[4][0]} - {top[4][1]}', False, 'White')
    except:
        pass
    quit_label = label.render('Quit', False, 'White', 'DarkGreen')
    quit_label_rect = quit_label.get_rect(topleft=(650, 500))

    running = True
    while running:
        pygame.display.update()

        try:
            screen.blit(top1, (WIDTH*0.1, HEIGHT*0.08))
        except:
            pass
        try:
            screen.blit(top2, (WIDTH*0.1, HEIGHT*0.25))
        except:
            pass
        try:
            screen.blit(top3, (WIDTH*0.1, HEIGHT*0.41))
        except:
            pass
        try:
            screen.blit(top4, (WIDTH*0.1, HEIGHT*0.58))
        except:
            pass
        try:
            screen.blit(top5, (WIDTH*0.1, HEIGHT*0.75))
        except:
            pass
        mouse = pygame.mouse.get_pos()
        screen.blit(quit_label, quit_label_rect)
        if quit_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
