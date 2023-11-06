import pygame
from bdconnect import top


def topfive():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
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
            screen.blit(top1, (200, 50))
        except:
            pass
        try:
            screen.blit(top2, (200, 150))
        except:
            pass
        try:
            screen.blit(top3, (200, 250))
        except:
            pass
        try:
            screen.blit(top4, (200, 350))
        except:
            pass
        try:
            screen.blit(top5, (200, 450))
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
