import random

import pygame

# Define constants for setup
SCREEN_SIZE = (1400, 900)
FRAME_RATE = 60

# Define constants for runtime
SCREEN_COLOR = (0, 0, 0)
BALL_SIZE = (100, 100)
BALL_START_POS = (random.randint(0, 1300), random.randint(0, 800))
PLAYER_START_POS = (random.randint(0, 1300), random.randint(0, 800))
TIME_INCREASE_CO_EFFICIENT = 5 * (10 ** -4)
START_SPEED_MIN = 3
START_SPEED_MAX = 5
SPEED_CAP = 5
ENEMY_SPAWN_NUMBER = 3

# Define constants for Ball class
SPEED_MIN = 3  # Minimum speed
SPEED_MAX = 5  # Maximum speed
RANDOM_INCREMENT = 3  # How much vel can change by every collision
ENEMY_IMAGE = "Assets/ball.png"  # What sprites to use for enemy and player
PLAYER_IMAGE = "Assets/player_ball.png"


# Ball class, enemy and player inherits from it
class Ball:
    def __init__(self, ball_type):
        self.ball_type = ball_type  # Stores if it is a player or enemy

        # Create surface and rect
        if self.ball_type == "Player":
            self.surface = pygame.image.load(PLAYER_IMAGE)
        elif self.ball_type == "Enemy":
            self.surface = pygame.image.load(ENEMY_IMAGE)
        else:
            raise Exception("Ball initialized of invalid ball_type")

        self.surface = pygame.transform.smoothscale(self.surface, BALL_SIZE)
        self.rect = self.surface.get_rect()

        self.vel = pygame.math.Vector2(random.randint(SPEED_MIN, SPEED_MAX),
                                       random.randint(SPEED_MIN, SPEED_MAX))

        # self.screen = screen  # Just use global screen
        # self.mask = pygame.mask.from_surface(self.surface)
        # self.vel = vel

    def collide(self, other):
        offset_x = other.rect[0] - self.rect[0]
        offset_y = other.rect[1] - self.rect[1]
        if not pygame.mask.from_surface(self.surface).overlap(pygame.mask.from_surface(other.surface),
                                                              (offset_x, offset_y)):
            # If it's not actually colliding with the other:
            return

        # This code is only reachable if the two are actually colliding, so we shouldn't need to check again
        if self.ball_type == "Player":  # It may help to check if other is an enemy, but that shouldn't be needed
            return True  # There was a collision
        # elif self.ball_type == "Enemy":
        #     # TODO: Add proper enemy-enemy collision code; do not return anything except None
        #     print("Enemy-Enemy collision detected")

        return

    def update(self):
        if self.ball_type == "Player":
            # Move to mouse position
            self.rect.center = pygame.mouse.get_pos()
        elif self.ball_type == "Enemy":
            any_wall_collision = False

            # Have one of these for each direction
            if self.rect.left <= 0:  # On collision with left wall
                any_wall_collision = True
                self.vel.x = abs(self.vel.x) * +1
            if self.rect.top <= 0:  # On collision with top wall
                any_wall_collision = True
                self.vel.y = abs(self.vel.y) * +1
            if self.rect.right >= SCREEN_SIZE[0]:  # On collision with right wall
                any_wall_collision = True
                self.vel.x = abs(self.vel.x) * -1
            if self.rect.bottom >= SCREEN_SIZE[1]:  # On collision with bottom wall
                any_wall_collision = True
                self.vel.y = abs(self.vel.y) * -1

            # If any collision occurs, run this code
            if any_wall_collision is True:
                # Constrain the value after randomizing it. Keeps it within bounds and changes by an amount. It has
                # - some casting a conditional to an int and remapping stuff to preserve travel direction after the
                # - absolute value in the sorted() fnc that constrains speed
                self.vel.x = sorted((SPEED_MIN,
                                     abs(self.vel.x) + random.randint(-RANDOM_INCREMENT, RANDOM_INCREMENT),
                                     SPEED_MAX))[1] * (int(self.vel.x > 0) * 2 - 1)
                self.vel.y = sorted((SPEED_MIN,
                                     abs(self.vel.y) + random.randint(-RANDOM_INCREMENT, RANDOM_INCREMENT),
                                     SPEED_MAX))[1] * (int(self.vel.y > 0) * 2 - 1)

            self.rect.move_ip(self.vel.x, self.vel.y)  # Move rect based off vel


def main():
    screen = pygame.display.set_mode([SCREEN_SIZE[0], SCREEN_SIZE[1]])  # Define pygame screen
    clock = pygame.time.Clock()  # Create a clock to manage frame rate

    # Initialize all balls
    balls = []  # Stores all balls
    # Initialize player
    balls += [Ball("Player")]
    # Initialize enemies
    for i in range(ENEMY_SPAWN_NUMBER):
        balls += [Ball("Enemy")]

    running = True
    is_dead = False  # TODO: change this to a death screen instead of ending the pygame process
    while running:
        is_dead = is_dead  # This is just to avoid an error because python scopes are weird, if is_dead was a mutable
        # (sry abt wht spc)  - object instead of just a var it wouldn't be mad, but that isn't worth it here

        clock.tick(FRAME_RATE)  # Wait until the next frame needs to be drawn
        screen.fill(SCREEN_COLOR)  # Draw the background

        for ball in balls:
            ball.update()
            for other in balls:  # For all the other balls
                if ball != other:  # Don't collide() with self
                    if ball.collide(other) is not None:
                        is_dead = True
            # Draw to screen
            screen.blit(ball.surface, ball.rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or is_dead:
                running = False


if __name__ == '__main__':
    main()
