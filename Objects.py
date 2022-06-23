import pygame
# from pygame import math
import random
import math

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1400

START_SPEED_MIN = 3
START_SPEED_MAX = 5
SPEED_MIN = -1
SPEED_MAX = 1
SPEED_CAP = 5


class Enitity:
    def __init__(self, surface: pygame.surface, vel: pygame.Vector2(), screen: pygame.display):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.vel = vel
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.surface)
        return


class Ball(Enitity):
    def __int__(self, surface: pygame.surface, vel: pygame.Vector2(), screen: pygame.display):
        self.surface = surface
        self.rect = self.surface.get_rect()
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.surface)
        self.vel = pygame.Vector2()
        self.vel += (random.randint(START_SPEED_MIN, START_SPEED_MAX),
                     random.randint(START_SPEED_MIN, START_SPEED_MAX))

    def collide(self, other, mask1, rect1, mask2, rect2):
        # self.vel
        # self.rect.center
        # other.vel
        # other.rect.center
        offset_x = rect2[0] - rect1[0]
        offset_y = rect2[1] - rect2[1]
        overlap = mask1.overlap(mask2, (offset_x, offset_y))
        if overlap:
            # Get vector magnitude (speed)
            ball_init_speed = self.vel.magnitude()

            # Get angle of normal line
            ball_pos_delta = pygame.Vector2((self.vel.x-other.vel.x), (self.vel.y-other.vel.y))
            collision_normal_angle = math.atan(ball_pos_delta.y / ball_pos_delta.x)
            if ball_pos_delta.x < 0 and ball_pos_delta.y < 0:
                collision_normal_angle += math.pi
            # get initial angle of travel from vel vector

            ball_init_travel_direc = math.atan(self.vel.y / self.vel.x)
            if self.vel.x < 0 and self.vel.y < 0:
                ball_init_travel_direc += math.pi
            # calculate difference in angle of normal line, and init travel direc

            collision_delta_theta = collision_normal_angle - ball_init_travel_direc
            # mirror init trav direc over norm ln to get final travel direc angle

            ball_final_travel_direc = ball_init_travel_direc + 2 * collision_delta_theta
            ball_final_travel_vec = pygame.Vector2(ball_init_speed * math.cos(ball_final_travel_direc),
                                                   ball_init_speed * math.sin(ball_final_travel_direc))
            self.vel = ball_final_travel_vec  # overwrite self.vel, so it will now travel in the correct direc
            return self.vel

    def movement(self):
        if self.rect.bottom >= SCREEN_HEIGHT:
            if self.vel.y >= SPEED_CAP or self.vel.y <= -SPEED_CAP:
                if self.vel.y >= SPEED_CAP:
                    self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MIN
                else:
                    self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MAX
            else:
                self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        if self.rect.top <= 0:
            if self.vel.y >= SPEED_CAP or self.vel.y <= -SPEED_CAP:
                if self.vel.y >= SPEED_CAP:
                    self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MIN
                else:
                    self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) - SPEED_MAX
            else:
                self.vel.y = (self.vel.y + ((-self.vel.y) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        if self.rect.left <= 0:
            if self.vel.x >= SPEED_CAP or self.vel.x <= -SPEED_CAP:
                if self.vel.x >= SPEED_CAP:
                    self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MIN
                else:
                    self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MAX
            else:
                self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        if self.rect.right >= SCREEN_WIDTH:
            if self.vel.x >= SPEED_CAP or self.vel.x <= -SPEED_CAP:
                if self.vel.x >= SPEED_CAP:
                    self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MIN
                else:
                    self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) - SPEED_MAX
            else:
                self.vel.x = (self.vel.x + ((-self.vel.x) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
        return self.vel

    def create_self(self):
        new_enemy = Ball
        return new_enemy
