import pygame


class Player:
    def __init__(self,
                 player_name,
                 player_speed: int = 10,
                 Jump_force: int = 30,
                 player_x: int = 100,
                 player_y: int = 400,
                 player_hp: int = 3
                 ):
        self.player_speed = player_speed
        self.Jump_force = Jump_force
        self.jump_count = Jump_force
        self.is_jump: bool = False
        self.player_x = player_x
        self.player_y = player_y
        self._player_hp = player_hp
        self.player_name = player_name

    def __bool__(self):
        """
        :return: bool живой или мертвый игрок
        """
        return self.player_hp > 0

    @property
    def player_hp(self) -> int:
        return self._player_hp

    @player_hp.setter
    def player_hp(self, value):
        if self:
            self._player_hp = value

    def switchJump(self):
        """
        Переключает состояние параметра is_jump на противоположное
        """
        self.is_jump = not self.is_jump

    def jump(self, keys: pygame.key.ScancodeWrapper):
        """
        Обработка прыжка
        """
        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
        else:
            if self.jump_count >= -self.Jump_force:
                if self.jump_count > 0:
                    self.player_y -= self.jump_count
                else:
                    self.player_y += abs(self.jump_count)
                self.jump_count -= 5
            else:
                self.is_jump = False
                self.jump_count = self.Jump_force

    def move(self, keys: pygame.key.ScancodeWrapper):
        """
        Передвижение игрока на право, на лево.
        """
        if keys[pygame.K_RIGHT] and self.player_x < 1100:
            self.player_x += self.player_speed
        elif keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.player_speed
