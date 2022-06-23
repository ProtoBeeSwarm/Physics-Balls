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
