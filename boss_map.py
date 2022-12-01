from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
class Boss_Map():
    def __init__(self):
        self.image = load_image('img/boss_map.png')
        self.bg = load_image('img/boss_map_bg.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(int(self.frame) * 290, 0,200,200,300,300,600,600)
        self.bg.draw(300,300,800,800)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        pass