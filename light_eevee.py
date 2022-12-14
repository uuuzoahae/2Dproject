from pico2d import *
import game_framework
import game_world
image = None
from random_eve_attack import Ev_Ball
class IDLE:
    @staticmethod
    def enter(self, event):
        # print('enter light IDLE')
        self.dir = 0
        self.dirud = 0
        self.timer = 1000
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass
    @staticmethod
    def exit(self, event):
        if event == SPACE:
            self.fire_ball()
        pass
    @staticmethod
    def draw(self):
        self.image.clip_draw(int(self.frame), 149, 30, 34, self.x +5, self.y + 3,35,35)
        pass


class RUN:
    def enter(self, event):
        print('enter light RUN')
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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)
        self.y = clamp(0, self.y, 600)
        pass
    def exit(self, event):
        self.face_dir = self.dir
        self.face_dirud = self.dirud
        if event == SPACE:
            self.fire_ball()

        pass
    def draw(self):

        # IDLE
        # self.image.clip_draw(int(self.frame), 149, 30, 34, self.x + 3, self.y + 3)

        if self.dir == 1:
            self.image.clip_composite_draw(55 + int(self.frame) * 33, 88, 31, 31, 0, 'h', self.x, self.y + 3, 35, 35)
            # self.right.clip_draw(7 + int(self.frame) * 24, 0, 25, 25, self.x, self.y, 40, 40)
        elif self.dir == -1:
            self.image.clip_draw(55 + int(self.frame) * 33, 88, 31, 31, self.x, self.y + 3, 35, 35)
            pass
        elif self.dirud == 1:
            self.image.clip_draw(54 + int(self.frame) * 25, 26, 28, 34, self.x, self.y + 5, 35, 35)
        elif self.dirud == -1:
            self.image.clip_draw(60 + int(self.frame) * 25, 149, 26, 34, self.x, self.y + 2,33,33)
        pass

# class ATTACK:
#     def enter(self):
#         pass
#     def do(self):
#         pass
#     def exit(self):
#         pass
#     def draw(self):
#         pass
#
class SLEEP:
    def enter(self, event):
        self.dir = 0
        self.dirud = 0
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pass
    def exit(self, event):
        pass
    def draw(self):
        self.image.clip_draw(362+ int(self.frame) * 30, 149, 30, 34, self.x, self.y + 2)
        pass

RD, LD, RU, LU, UD, UU, DD, DU, TIMER, SPACE = range(10)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD, (SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYUP, SDLK_RIGHT): RU, (SDL_KEYUP, SDLK_LEFT): LU,
(SDL_KEYDOWN, SDLK_UP) : UD, (SDL_KEYUP, SDLK_UP) : UU,
(SDL_KEYDOWN, SDLK_DOWN) : DD, (SDL_KEYUP, SDLK_DOWN) : DU,
(SDL_KEYDOWN, SDLK_SPACE) : SPACE
}

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

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3

class Light_Eve():
    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.x, self.y = 300, 300
        self.hp = 300
        self.dir = 0
        self.dirud = 0
        self.frame = 0
        self.image = load_image('img/character_light.png')
        self.name = 'LIGHT'
        self.q = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)
        self.ui = Boss_UI(self.x, self.y, self.hp)

    def update(self):
        self.ui = Boss_UI(self.x, self.y, self.hp)
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.ui.draw()
        # draw_rectangle(*self.get_bb())

    def fire_ball(self):
        print('FIRE BALL')
        if self.dir == 1 or self.dir == -1:
            ball = Ev_Ball(self.x, self.y, self.face_dir,'dir')
            game_world.add_object(ball, 1)
            game_world.add_collision_pairs(None, ball, 'boss:ball')
        elif self.dirud == 1 or self.dirud == -1:
            ball = Ev_Ball(self.x, self.y, self.face_dirud,'dirud')
            game_world.add_object(ball, 1)
            game_world.add_collision_pairs(None, ball, 'boss:ball')

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 20

    def handle_collision(self, other, group):
        if group == "rand_eve:water":
            self.hp -= 50
            print('eve hp = ', self.hp)
            game_world.remove_object(other)
        pass

class Boss_UI:
    image = None
    def __init__(self, x, y, hp):
        if Boss_UI.image == None:
            Boss_UI.image = load_image('img/heart2.png')

        self.frame = 0
        self.x = x
        self.y = y
        self.hp = hp


    def draw(self):

        if self.hp <= 300 and self.hp > 200:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x + 18, self.y+25,22,22)
        elif self.hp <= 200 and self.hp > 100:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
        elif self.hp <= 100 and self.hp > 0:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)


    def update(self):
        self.frame += game_framework.frame_time
        pass

    def handle_event(self):
        pass

    def play_sound(self):
        pass
