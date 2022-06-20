import pygame
import random
from AvoiderObjects import Ball

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1400
SCREEN_COLOR = (0, 0, 0)

BALL_SIZE = (100, 100)

BALL_START_POS = (random.randint(0, 1300), random.randint(0, 800))
PLAYER_START_POS = (random.randint(0, 1300), random.randint(0, 800))

FRAME_RATE = 60

TIME_INCREASE_CO_EFFICIENT = 5 * (10 ** -4)
START_SPEED_MIN = 3
START_SPEED_MAX = 5
SPEED_MIN = -1
SPEED_MAX = 1
SPEED_CAP = 5
ENEMY_SPAWN_NUMBER = 3


def pixel_collision_player(mask1, rect1, mask2, rect2):
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap


def ball_create(image, size, location, screen):
    ball = pygame.image.load(image)
    ball = pygame.transform.smoothscale(ball, size)
    screen.blit(ball, location)
    return ball


def ball_rect_create(ball, loc_start_pos):
    ball_rect = ball.get_rect()
    ball_rect.move_ip(loc_start_pos)
    return ball_rect


#def velocity_update(ball_rect, x_vel, y_vel):
    # #if ball_rect.bottom >= SCREEN_HEIGHT:
    #     #if y_vel >= SPEED_CAP or y_vel <= -SPEED_CAP:
    #         if y_vel >= SPEED_CAP:
    #             y_vel = (y_vel + ((-y_vel) * 2)) - SPEED_MIN
    #         else:
    #             y_vel = (y_vel + ((-y_vel) * 2)) - SPEED_MAX
    #     else:
    #         y_vel = (y_vel + ((-y_vel) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
    # if ball_rect.top <= 0:
    #     if y_vel >= SPEED_CAP or y_vel <= -SPEED_CAP:
    #         if y_vel >= SPEED_CAP:
    #             y_vel = (y_vel + ((-y_vel) * 2)) - SPEED_MIN
    #         else:
    #             y_vel = (y_vel + ((-y_vel) * 2)) - SPEED_MAX
    #     else:
    #         y_vel = (y_vel + ((-y_vel) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
    # if ball_rect.left <= 0:
    #     if x_vel >= SPEED_CAP or x_vel <= -SPEED_CAP:
    #         if x_vel >= SPEED_CAP:
    #             x_vel = (x_vel + ((-x_vel) * 2)) - SPEED_MIN
    #         else:
    #             x_vel = (x_vel + ((-x_vel) * 2)) - SPEED_MAX
    #     else:
    #         x_vel = (x_vel + ((-x_vel) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
    # if ball_rect.right >= SCREEN_WIDTH:
    #     if x_vel >= SPEED_CAP or x_vel <= -SPEED_CAP:
    #         if x_vel >= SPEED_CAP:
    #             x_vel = (x_vel + ((-x_vel) * 2)) - SPEED_MIN
    #         else:
    #             x_vel = (x_vel + ((-x_vel) * 2)) - SPEED_MAX
    #     else:
    #         x_vel = (x_vel + ((-x_vel) * 2)) + random.randint(SPEED_MIN, SPEED_MAX)
    #return x_vel, y_vel


# def update_ball(ball, ball_rect, x_vel, y_vel, screen):
#     ball_rect.move_ip(x_vel, y_vel)
#     screen.blit(ball, ball_rect)
#     x_vel, y_vel = velocity_update(ball_rect, x_vel, y_vel)
#     return x_vel, y_vel


def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    enemies = []

    for i in range(ENEMY_SPAWN_NUMBER):
        ball_create("ball.png", BALL_SIZE, BALL_START_POS, screen)
        #BALL_START_POS = (random.randint(0, 1300), random.randint(0, 800))
        enemies = enemies + [Ball]


    player_ball = ball_create("player_ball.png", BALL_SIZE, PLAYER_START_POS, screen)
    player_ball_rect = ball_rect_create(player_ball, PLAYER_START_POS)
    player_mask = pygame.mask.from_surface(player_ball)



    pygame.display.flip()

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(FRAME_RATE)

        screen.fill(SCREEN_COLOR)

        global SPEED_CAP
        SPEED_CAP = SPEED_CAP + TIME_INCREASE_CO_EFFICIENT

        pos = pygame.mouse.get_pos()
        player_ball_rect.center = pos

        Ball.movement(Ball)
        Ball.collide()

        screen.blit(player_ball, player_ball_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
