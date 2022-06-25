# Old ball collision code:

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

# New colision code, needs to be fixed later
# def collide(self, other, mask1, rect1, mask2, rect2):
#     # self.vel
#     # self.rect.center
#     # other.vel
#     # other.rect.center
#     offset_x = rect2[0] - rect1[0]
#     offset_y = rect2[1] - rect2[1]
#     overlap = mask1.overlap(mask2, (offset_x, offset_y))
#     if overlap:
#         # Get vector magnitude (speed)
#         ball_init_speed = self.vel.magnitude()
#
#         # Get angle of normal line
#         ball_pos_delta = pygame.Vector2((self.vel.x-other.vel.x), (self.vel.y-other.vel.y))
#         collision_normal_angle = math.atan(ball_pos_delta.y / ball_pos_delta.x)
#         if ball_pos_delta.x < 0 and ball_pos_delta.y < 0:
#             collision_normal_angle += math.pi
#         # get initial angle of travel from vel vector
#
#         ball_init_travel_direc = math.atan(self.vel.y / self.vel.x)
#         if self.vel.x < 0 and self.vel.y < 0:
#             ball_init_travel_direc += math.pi
#         # calculate difference in angle of normal line, and init travel direc
#
#         collision_delta_theta = collision_normal_angle - ball_init_travel_direc
#         # mirror init trav direc over norm ln to get final travel direc angle
#
#         ball_final_travel_direc = ball_init_travel_direc + 2 * collision_delta_theta
#         ball_final_travel_vec = pygame.Vector2(ball_init_speed * math.cos(ball_final_travel_direc),
#                                                ball_init_speed * math.sin(ball_final_travel_direc))
#         self.vel = ball_final_travel_vec  # overwrite self.vel, so it will now travel in the correct direc
#         return self.vel