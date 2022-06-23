import random
import pygame

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


# Create surface from the ball image
def ball_create(image, size, location, screen):
    ball = pygame.image.load(image)
    ball = pygame.transform.smoothscale(ball, size)
    screen.blit(ball, location)
    return ball


# Create new ball rectangle from a ball surface
def ball_rect_create(ball, loc_start_pos):
    ball_rect = ball.get_rect()
    ball_rect.move_ip(loc_start_pos)
    return ball_rect


def update_ball(ball, ball_rect, x_vel, y_vel, screen):
    ball_rect.move_ip(x_vel, y_vel)
    screen.blit(ball, ball_rect)
    x_vel, y_vel = velocity_update(ball_rect, x_vel, y_vel)
    return x_vel, y_vel


def main():
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # Define pygame screen
    clock = pygame.time.Clock()  # Create a clock to manage frame rate

    # Initialize Enemy ball
    enemies = []
    for i in range(ENEMY_SPAWN_NUMBER):
        # ball_create("player_ball.png", BALL_SIZE, BALL_START_POS, screen)
        # new_ball = Ball("player_ball.png", pygame.math.Vector2(2, 3), screen)
        enemies = enemies + [Ball(ball_create("player_ball.png", BALL_SIZE, BALL_START_POS, screen),
                                  pygame.math.Vector2(2, 3), screen)]
        # enemies = enemies + [ball_create("player_ball.png", BALL_SIZE, BALL_START_POS, screen)]

    # Initialize Player Ball
    player_ball = ball_create("player_ball.png", BALL_SIZE, PLAYER_START_POS, screen)
    player_ball_rect = ball_rect_create(player_ball, PLAYER_START_POS)
    player_mask = pygame.mask.from_surface(player_ball)
    pygame.display.flip()

    # Once per frame code
    running = True
    while running:
        # wait until the next frame needs to be drawn
        clock.tick(FRAME_RATE)

        # Increase max speed for balls
        global SPEED_CAP
        SPEED_CAP = SPEED_CAP + TIME_INCREASE_CO_EFFICIENT

        # Move player ball to mouse's position
        pos = pygame.mouse.get_pos()
        player_ball_rect.center = pos

        # Move balls & once implemented, handle collisions
        for enemy in enemies:
            enemy.move()
        # Ball.collide()  # For now do not collide as that has not been implemented

        # Draw to screen
        screen.fill(SCREEN_COLOR)
        screen.blit(player_ball, player_ball_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
