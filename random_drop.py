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
class Random_drop():
    image = None
    def __init__(self):
        # 물방울 랜덤 선택
        self.frame = random.choice([0, 17, 34, 50])
        print('ran frame = ', self.frame)
        
        self.x, self.y = random.randint(0 ,700) , random.randint(300 ,600)
        # self.image = load_image('water_drop.png')
        if Random_drop.image == None:
            Random_drop.image = load_image('img/random_drop.png')
    def update(self):
        if self.y >= -300:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        elif self.y <= -300:
            self.y = random.randint(500, 700)
    def draw(self):
        # self.image.clip_draw(0, 0, 70, 35, self.x, self.y)
        self.image.clip_draw(self.frame, 0, 15, 20, self.x, self.y, 18, 18)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-9, self.y-15, self.x+9, self.y+15

    def handle_collision(self, other, group):
        if group == 'eve:water':

        pass