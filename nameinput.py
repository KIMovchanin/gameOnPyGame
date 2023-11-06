import pygame
import game

name = []


def entername():
    pygame.init()
    screen = pygame.display.set_mode((1067, 600))
    bg = pygame.image.load('Materials/Images/back_menu.jpg')

    clock = pygame.time.Clock()

    label = pygame.font.Font(None, 40)
    user_input = 'John Doe'
    please_write = label.render('Please click on the square and write your nickname: ', False, 'Black')
    start_button = label.render('Start', False, 'White', 'DarkGreen')
    start_button_rect = start_button.get_rect(topleft=(900, 500))

    input_rect = pygame.Rect(500, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')

    active = False

    while True:
        pygame.display.update()

        screen.blit(bg, (0, 0))
        # screen.fill((0, 0, 0))
        screen.blit(please_write, (200, 100))
        text_surface = label.render(user_input, False, 'DarkGreen')
        screen.blit(text_surface, (input_rect.x + 3, input_rect.y + 3))
        screen.blit(start_button, start_button_rect)

        for el in pygame.event.get():
            if el.type == pygame.QUIT:
                pygame.quit()
                break

            if el.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(el.pos):
                    active = True
                    user_input = ''
                else:
                    active = False

            if el.type == pygame.KEYDOWN:
                if active:
                    if el.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += el.unicode

        if active:
            color = color_active
        else:
            color = color_passive
        # цифра здесь позволяет нам не залить весь квадрат текстом, с только создать обводку
        pygame.draw.rect(screen, color, input_rect, 2)

        input_rect.w = max(100, text_surface.get_width() + 10)

        mouse = pygame.mouse.get_pos()

        if start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            name.append(user_input)
            game.play()
            pygame.quit()
            break

        # pygame.display.flip()
        clock.tick(14)
