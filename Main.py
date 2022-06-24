import math
import random

import pygame

# Define constants for setup
SCREEN_SIZE = (1400, 900)
FRAME_RATE = 60

# Define constants for runtime
SCREEN_COLOR = (196, 175, 144)  # c4af90
BALL_SIZE = (100, 100)
BALL_START_POS = (random.randint(0, 1300), random.randint(0, 800))
PLAYER_START_POS = (random.randint(0, 1300), random.randint(0, 800))
TIME_INCREASE_CO_EFFICIENT = 5 * (10 ** -4)
# START_SPEED_MIN = 3
# START_SPEED_MAX = 5
# SPEED_CAP = 5
ENEMY_SPAWN_NUMBER = 4

# Define constants for Ball class
SPEED_MIN = 3  # Minimum speed
SPEED_MAX = 7  # Maximum speed
RANDOM_INCREMENT = 3  # How much vel can change by every collision
ENEMY_IMAGE = "Assets/Predator.png"  # What sprites to use for enemy and player
PLAYER_IMAGE = "Assets/Prey.png"


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
        self.rect = self.surface.get_rect()  # Make new rect

        self.rect.move_ip(random.randint(0, SCREEN_SIZE[0] - self.rect.width),  # Move to random position
                          random.randint(0, SCREEN_SIZE[1] - self.rect.height))

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
        elif self.ball_type == "Enemy":

            # Get vector magnitude (speed)
            ball_init_speed = self.vel.magnitude()

            # Get angle of normal line
            ball_pos_delta = pygame.Vector2((self.vel.x - other.vel.x), (self.vel.y - other.vel.y))
            if ball_pos_delta.x == 0:  # This is just to avoid div by 0, could be done better though
                ball_pos_delta.x = 1
            collision_normal_angle = math.atan(ball_pos_delta.y / ball_pos_delta.x)
            if ball_pos_delta.x < 0 and ball_pos_delta.y < 0:
                collision_normal_angle += math.pi
            # get initial angle of travel from vel vector

            ball_init_travel_direction = math.atan(self.vel.y / self.vel.x)
            if self.vel.x < 0 and self.vel.y < 0:
                ball_init_travel_direction += math.pi
            # calculate difference in angle of normal line, and init travel direction

            collision_delta_theta = collision_normal_angle - ball_init_travel_direction
            # mirror init trav direction over norm ln to get final travel direction angle

            ball_final_travel_direction = ball_init_travel_direction + 2 * collision_delta_theta
            ball_final_travel_vec = pygame.Vector2(ball_init_speed * math.cos(ball_final_travel_direction),
                                                   ball_init_speed * math.sin(ball_final_travel_direction))
            self.vel = ball_final_travel_vec  # overwrite self.vel, so it will now travel in the correct direction

            self.rect.move_ip(self.vel.x, self.vel.y)  # Move rect based off vel, so it doesn't double collide

            # Get the angle of the collision:
            # if (self.vel.x - other.vel.x) != 0:
            #     cos_theta = math.cos(math.atan((self.vel.y - other.vel.y) / (self.vel.x - other.vel.x)))
            # else:  # In the case of divide by zero, just use the exact value, being zero
            #     cos_theta = 0  # $\lim_{b \to 0} \cos{(\tan^{-1}{(\frac{1}{b})})} = \frac{\pi}{2}$
            #
            # # Lose the force of self.vel*cos(θ)
            # self.vel -= self.vel * cos_theta
            # # Gain the force of other.vel*cos(θ)
            # self.vel += other.vel * cos_theta

            # self.rect.move_ip(self.vel.x, self.vel.y)  # Move rect based off vel

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
            pygame.draw.line(screen, (255, 255, 0), ball.rect.center, ball.rect.center + ball.vel * 15)
            vector_scaler = 30  # I am unreasonably proud of that joke, and it's not even that good
            pygame.draw.line(screen, (255, 0, 0), ball.rect.center, pygame.math.Vector2(ball.rect.center[0] + ball.vel.x * vector_scaler, ball.rect.center[1]))
            pygame.draw.line(screen, (0, 255, 0), ball.rect.center, pygame.math.Vector2(ball.rect.center[0], ball.rect.center[1] + ball.vel.y * vector_scaler))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or is_dead:
            # if event.type == pygame.QUIT:  # Man I miss being able to use multi line comments inside a single line :(
                running = False


if __name__ == '__main__':
    main()
