# from pygame import math
import random

import pygame

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1400

START_SPEED_MIN = 3
START_SPEED_MAX = 5
SPEED_MIN = -1
SPEED_MAX = 1
SPEED_CAP = 5


class Ball:
    def __init__(self, surface: pygame.surface, vel: pygame.Vector2(), screen: pygame.display):
        self.surface = surface
        self.rect = surface.get_rect()
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.surface)
        self.vel = vel
        self.vel += (random.randint(START_SPEED_MIN, START_SPEED_MAX),
                     random.randint(START_SPEED_MIN, START_SPEED_MAX))

    def move(self):
        print(self.vel)
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     if self.vel.y >= SPEED_CAP or self.vel.y <= -SPEED_CAP:
        #         if self.vel.y >= SPEED_CAP:
        #             self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MIN
        #         else:
        #             self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MAX
        #     else:
        #         self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        # if self.rect.top <= 0:
        #     if self.vel.y >= SPEED_CAP or self.vel.y <= -SPEED_CAP:
        #         if self.vel.y >= SPEED_CAP:
        #             self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MIN
        #         else:
        #             self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MAX
        #     else:
        #         self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        # if self.rect.left <= 0:
        #     if self.vel.x >= SPEED_CAP or self.vel.x <= -SPEED_CAP:
        #         if self.vel.x >= SPEED_CAP:
        #             self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MIN
        #         else:
        #             self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MAX
        #     else:
        #         self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        # if self.rect.right >= SCREEN_WIDTH:
        #     if self.vel.x >= SPEED_CAP or self.vel.x <= -SPEED_CAP:
        #         if self.vel.x >= SPEED_CAP:
        #             self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MIN
        #         else:
        #             self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MAX
        #     else:
        #         self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        # # return self.vel
        return

    # def create_self(self):
    #     new_enemy = Ball
    #     return new_enemy
