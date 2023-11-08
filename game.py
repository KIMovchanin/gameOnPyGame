import animplayer as ap
import animzombie as az
import pygame
import bdconnect as db
import bullet as bl
from math import ceil
import win
import nameinput
import topfive
import menu
import player as pl
from screensettings import WIDTH, HEIGHT

bullets = []
zombie_list_in_game = []


def play():
    # добавили класс Clock в игру, чтобы в конце программы сделать "тик" в игре медленнее
    clock = pygame.time.Clock()
    # обаятельный метод в начале для инициализации игры
    pygame.init()
    pygame.mixer.init()
    # указываем размер экрана в формате (ширина, высота)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.mixer.init(44100, -16, 2, 2048)
    # добавляем название для приложения
    pygame.display.set_caption("PyGame Injinerium")
    # подгружаю картинку в проект
    ICON = pygame.image.load('Materials/Images/inj.jpg').convert()
    # устанавливаю картинку в качестве иконки
    pygame.display.set_icon(ICON)
    bg = pygame.image.load('Materials/Images/back.jpg').convert()

    zombie = az.ZOMBIE_WALK_L[0]

    # создали счётчик для перебора анимаций картинок персонажа
    player_anim_count_run = 0
    player_anim_count_idle = 0
    zombie_anim_count_walk = 0
    bg_x = 0

    # создаём переменные для передвижения игрока
    _player_name = str(nameinput.name[0])
    player = pl.Player(_player_name)
    print(player.player_name)

    # подгружаем музыку
    bg_sound = pygame.mixer.Sound('Materials/Music/ForestWalk.mp3')
    bg_sound.play()  # запускаем музыку

    #  создали таймер для спавна зомби
    zombie_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(zombie_timer, 2500)

    label = pygame.font.Font('Materials/Fonts/Quicksand-VariableFont_wght.ttf', 40)
    lose_label = label.render('You lose!', False, 'DarkRed')

    restart_label = label.render('Play again', False, 'White', 'DarkGreen')
    restart_label_rect = restart_label.get_rect(topleft=(WIDTH*0.42, HEIGHT*0.58))

    menu_label = label.render('Go to menu', False, 'White', 'DarkGreen')
    menu_label_rect = menu_label.get_rect(topleft=(WIDTH*0.4125, HEIGHT*0.83))

    top_label = label.render('Top 5 players', False, 'White', 'DarkGreen')
    top_label_rect = top_label.get_rect(topleft=(WIDTH*0.66, HEIGHT*0.66))

    ammo_max = 7
    ammo = ammo_max
    score = 1
    timer = 0
    time = 420

    # создаём переменную для понимания проиграл игрок или нет
    gameplay = True

    running = True
    while running:

        if timer >= 420:
            db.addindb(player.player_name, ceil(timer / 14), score + ((ceil(timer / 14)) * 10) - 1)
            bg_sound.stop()
            zombie_list_in_game.clear()
            bullets.clear()
            pygame.mixer.quit()
            win.win()
            break

        keys = pygame.key.get_pressed()
        timer += 1
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + WIDTH, 0))
        time = time - 1
        time_label = label.render(f'Time: {str(int(time / 14))}', False, 'gray15')
        screen.blit(time_label, (0, 0))
        ammo_label = label.render(f'Ammo: {str(ammo)}', False, 'gray15')
        screen.blit(ammo_label, (WIDTH*0.83, 0))

        # грубо говоря всё работает, пока игрок жив
        if gameplay:

            # создаём хитбокс игрока
            player_rect = ap.RUN_RIGHT[0].get_rect(
                topleft=(player.player_x, player.player_y))

            if zombie_list_in_game:
                for (i, el) in enumerate(zombie_list_in_game):
                    screen.blit(az.ZOMBIE_WALK_L[zombie_anim_count_walk], el)
                    el.x -= 10

                    if el.x < -70:
                        zombie_list_in_game.pop(i)

                    # а теперь прописываем что происходит при соприкосновении игрока с зомби
                    if player_rect.colliderect(el):
                        player.player_hp -= 1
                        if player:
                            bg_sound.stop()
                            gameplay = False

            if keys[pygame.K_RIGHT]:
                screen.blit(ap.RUN_RIGHT[player_anim_count_run], (player.player_x, player.player_y))
            elif keys[pygame.K_LEFT]:
                screen.blit(ap.RUN_LEFT[player_anim_count_run], (player.player_x, player.player_y))
            else:
                screen.blit(ap.IDLE[player_anim_count_idle], (player.player_x, player.player_y))

            player.move(keys=keys)

            player.jump(keys=keys)

            # меняем "фрейм" к которому мы обращаемся
            if player_anim_count_run == len(ap.RUN_RIGHT) - 1:
                player_anim_count_run = 0
            else:
                player_anim_count_run += 1

            if player_anim_count_idle == len(ap.IDLE) - 1:
                player_anim_count_idle = 0
            else:
                player_anim_count_idle += 1

            if bullets:
                for (i, el) in enumerate(bullets):
                    screen.blit(bl.BULLET_R[0], (el.x, el.y))
                    el.x += 70

                    if el.x > WIDTH+20:
                        bullets.pop(i)

                    if zombie_list_in_game:
                        for (index, enemy) in enumerate(zombie_list_in_game):
                            if el.colliderect(enemy):
                                zombie_list_in_game.pop(index)
                                score += 100
                                if bullets:
                                    bullets.pop(i)
                                else:
                                    pass

        else:
            # заполняем экран таким цветом при проигрыше
            screen.fill('Black')
            screen.blit(lose_label, (WIDTH*0.43, HEIGHT*0.43))
            screen.blit(restart_label, restart_label_rect)
            screen.blit(top_label, top_label_rect)
            screen.blit(menu_label, menu_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player.player_x = 100
                time = 420
                zombie_list_in_game.clear()
                bg_sound.play()
                bullets.clear()
                ammo = ammo_max
                timer = 0
            elif top_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                db.addindb(player.player_name, ceil(timer / 14), score + ((ceil(timer / 14)) * 10) - 1)
                topfive.topfive()
                break
            elif menu_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                db.addindb(player.player_name, ceil(timer / 14), score + ((ceil(timer / 14)) * 10) - 1)
                menu.startmenu()
                break

        # обновление экрана
        pygame.display.update()

        # чтобы закрыть экран
        for event in pygame.event.get():  # за счёт метода pygame.event.get() мы получаем список из всех возможных
            # событий
            if event.type == pygame.QUIT:  # если событие это нажатие на выход
                running = False
                print(score)
                print(ceil(timer / 14))
                # записываю всё в бд
                db.addindb(player.player_name, ceil(timer / 14), score + ((ceil(timer / 14)) * 10) - 1)
                pygame.quit()
                break

            # при срабатывании USEREVENT добавляем в список коллайдер от зомби, по координатам которого мы будем
            # рисовать на экране самого зомби
            if event.type == zombie_timer:
                zombie_list_in_game.append(zombie.get_rect(topleft=(WIDTH+20, HEIGHT*0.71)))
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and ammo > 0:
                bullets.append(bl.BULLET_R[0].get_rect(topleft=(player.player_x + 20, player.player_y + 35)))
                ammo -= 1
        clock.tick(14)
