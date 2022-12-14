import random
from pico2d import *

import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#
# TIME_PER_ACTION = 0.3
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 3
class Water_drop():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0 ,700) , random.randint(300 ,600)
        # self.image = load_image('water_drop.png')
        if Water_drop.image == None:
            Water_drop.image = load_image('img/water_drop.png')
    def update(self):
        if self.y >= -300:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.y <= -300:
            self.y = random.randint(500, 700)
    def draw(self):
        self.image.clip_draw(0, 0, 1000, 1000, self.x, self.y, 30, 30)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-9, self.y-15, self.x+9, self.y+15

    def handle_collision(self, other, group):
        pass