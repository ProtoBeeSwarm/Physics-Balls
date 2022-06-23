# Import as nessecary
import pygame
import random
from Objects import Ball

# Define constants for setup
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1400
FRAME_RATE = 60

# Define constants for runtime
SCREEN_COLOR = (0, 0, 0)
BALL_SIZE = (100, 100)
BALL_START_POS = (random.randint(0, 1300), random.randint(0, 800))
PLAYER_START_POS = (random.randint(0, 1300), random.randint(0, 800))
TIME_INCREASE_CO_EFFICIENT = 5 * (10 ** -4)
START_SPEED_MIN = 3
START_SPEED_MAX = 5
SPEED_MIN = -1
SPEED_MAX = 1
SPEED_CAP = 5
ENEMY_SPAWN_NUMBER = 3

# Check if two pygame objects are overlapping
def pixel_collision_player(mask1, rect1, mask2, rect2):
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap

# Create new ball object
def ball_create(image, size, location, screen):
    ball = pygame.image.load(image)
    ball = pygame.transform.smoothscale(ball, size)
    screen.blit(ball, location)
    return ball

# Create new ball rectangle
def ball_rect_create(ball, loc_start_pos):
    ball_rect = ball.get_rect()
    ball_rect.move_ip(loc_start_pos)
    return ball_rect


# def update_ball(ball, ball_rect, x_vel, y_vel, screen):
#     ball_rect.move_ip(x_vel, y_vel)
#     screen.blit(ball, ball_rect)
#     x_vel, y_vel = velocity_update(ball_rect, x_vel, y_vel)
#     return x_vel, y_vel


def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # Define pygame screen
    clock = pygame.time.Clock()  # Create a clock to manage frame rate

    # Generate balls
    enemies = []
    for i in range(ENEMY_SPAWN_NUMBER):
        ball_create("ball.png", BALL_SIZE, BALL_START_POS, screen)
        enemies = enemies + [Ball]

    # Draw balls to screen
    player_ball = ball_create("player_ball.png", BALL_SIZE, PLAYER_START_POS, screen)
    player_ball_rect = ball_rect_create(player_ball, PLAYER_START_POS)
    player_mask = pygame.mask.from_surface(player_ball)
    pygame.display.flip()



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
