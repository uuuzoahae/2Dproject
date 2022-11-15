from pico2d import *

import game_framework
import game_world
from fire_ball import Ball
RD, LD, RU, LU, UD, UU, DD, DU, TIMER, SPACE = range(10)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD, (SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYUP, SDLK_RIGHT): RU, (SDL_KEYUP, SDLK_LEFT): LU,
(SDL_KEYDOWN, SDLK_UP) : UD, (SDL_KEYUP, SDLK_UP) : UU,
(SDL_KEYDOWN, SDLK_DOWN) : DD, (SDL_KEYUP, SDLK_DOWN) : DU,
(SDL_KEYDOWN, SDLK_SPACE) : SPACE
}

class IDLE:
    @staticmethod
    def enter(self, event):
        print("ENTER IDLE")
        self.dir = 0
        self.dirud = 0
        self.timer = 1000
        pass
    @staticmethod
    def do(self):
        # self.frame = (self.frame + 1) % 3
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.timer -= 50
        if self.timer == 0:
            self.add_event(TIMER)
        pass
    @staticmethod
    def exit(self, event):
        print("EXIT IDLE")
        if event == SPACE:
            self.fire_ball()
        pass
    @staticmethod
    def draw(self):
        if self.dir == 0:
            self.image.clip_draw(78 + int(self.frame) * 25, 187, 25, 25, self.x, self.y, 40, 40)
        pass

class RUN:
    def enter(self, event):
        print("RUN ENTER")

        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == UD:
            self.dirud += 1
        elif event == UU:
            self.dirud -= 1
        elif event == DD:
            self.dirud -= 1
        elif event == DU:
            self.dirud += 1
        pass
    def do(self):
        # self.frame = (self.frame + 1) % 3
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)
        pass
    def exit(self, event):
        self.face_dir = self.dir
        self.face_dirud = self.dirud
        print("RUN EXIT")
        if event == SPACE:
            self.fire_ball()
        pass
    def draw(self):

        # if self.dir == 0 and self.dirud > 0:
        #     self.image.clip_draw(78 + self.frame * 25, 80, 25, 25, self.x, self.y, 40, 40)
        # if self.dir == 0:
        #     self.image.clip_draw(78 + self.frame * 25, 187, 25, 25, self.x, self.y, 40, 40)
        if self.dir == 1:
            self.right.clip_draw(7 + int(self.frame) * 24, 0, 25, 25, self.x, self.y, 40, 40)
            # self.image.clip_composite_draw(7 + self.frame*24, 0, 25, 25,
            #                                0,'v',self.x,self.y, 40, 40)
        elif self.dir == -1:
            self.image.clip_draw(77 + int(self.frame) * 25, 160, 25, 25, self.x, self.y, 40, 40)
        elif self.dirud == 1:
            self.image.clip_draw(78 + int(self.frame) * 25, 80, 25, 25, self.x, self.y, 40, 40)
        elif self.dirud == -1:
            self.image.clip_draw(78 + int(self.frame) * 25, 187, 25, 25, self.x, self.y, 40, 40)
        pass

class ATTACK:
    def enter(self):
        pass
    def do(self):
        pass
    def exit(self):
        pass
    def draw(self):
        pass

class SLEEP:
    def enter(self, event):
        self.dir = 0
        self.dirud = 0
        print("SLEEP ENTER")
        pass
    def do(self):
        # self.frame = ( 1 + self.frame) % 2
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pass
    def exit(self, event):
        print("SLEEP EXIT")
        pass
    def draw(self):
        self.image.clip_draw(430 + int(self.frame) * 30, 190, 28, 28, self.x-2, self.y-2,43,43)
        #43, 43)
        pass

next_state = {
SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, UU: RUN, DD: RUN, DU: RUN, TIMER:SLEEP, SPACE:SLEEP},
IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, UU: RUN, DD: RUN, DU: RUN, TIMER:SLEEP, SPACE:IDLE},
RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE, TIMER:RUN, SPACE:RUN}
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
class Eve():
    def add_event(self, key_event):
        self.q.insert(0, key_event)
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.x, self.y = 300, 300
        self.dir = 0
        self.dirud = 0
        self.face_dir = 1
        self.face_dirud = 1
        self.frame = 0
        self.image = load_image('character_eevee.png')
        self.right = load_image('character_eevee_right.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 3
        # self.x += self.dir * 5
        # self.y += self.dirud * 5

    def draw(self):
        self.cur_state.draw(self)

    def fire_ball(self):
        print('FIRE BALL')
        if self.dir == 1 or self.dir == -1:
            ball = Ball(self.x, self.y, self.face_dir * 2)
            game_world.add_object(ball, 1)
        elif self.dirud == 1 or self.dirud == -1:
            ball = Ball(self.x, self.y , self.face_dirud * 2)
            game_world.add_object(ball, 1)


        # 상하
        # if self.dir == 0 and self.dirud > 0:
        #     self.image.clip_draw(78 + self.frame * 25, 80, 25, 25, self.x, self.y, 40, 40)

        # 정지 또는 걷기

        # elif self.dir == 0:
        #     self.image.clip_draw(78 + self.frame * 25, 187, 25, 25, self.x, self.y, 40, 40)
        # elif self.dir > 0:
        #     self.right.clip_draw(7 + self.frame * 24, 0, 25, 25, self.x, self.y, 40, 40)
        # elif self.dir < 0:
        #     self.image.clip_draw(77 + self.frame * 25, 160, 25, 25, self.x, self.y, 40, 40)



    # def handle_event(self, event):
    #     if event.type == SDL_KEYDOWN:
    #         match event.key:
    #             case pico2d.SDLK_LEFT:
    #                 self.dir -= 1
    #             case pico2d.SDLK_RIGHT:
    #                 self.dir += 1
    #     elif event.type == SDL_KEYUP:
    #         match event.key:
    #             case pico2d.SDLK_LEFT:
    #                 self.dir += 1
    #                 self.face_dir = -1
    #             case pico2d.SDLK_RIGHT:
    #                 self.dir -= 1
    #                 self.face_dir = 1