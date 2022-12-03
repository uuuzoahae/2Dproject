from pico2d import *
import game_framework
import game_world
import boss_state
import title_state
from fire_ball import Ball

RD, LD, RU, LU, UD, UU, DD, DU, TIMER, SPACE= range(10)
key_event_table = {
(SDL_KEYDOWN, SDLK_RIGHT): RD, (SDL_KEYDOWN, SDLK_LEFT): LD,
(SDL_KEYUP, SDLK_RIGHT): RU, (SDL_KEYUP, SDLK_LEFT): LU,
(SDL_KEYDOWN, SDLK_UP) : UD, (SDL_KEYUP, SDLK_UP) : UU,
(SDL_KEYDOWN, SDLK_DOWN) : DD, (SDL_KEYUP, SDLK_DOWN) : DU,
(SDL_KEYDOWN, SDLK_SPACE) : SPACE
}


table = {"SLEEP": {"WATER": "HURT"},
         "IDLE": {"WATER": "HURT"},
         "RUN": {"WATER": "HURT"},
         "HURT": {"WATER": "HURT"}}

# name = {'EVE','LIGHT','WATER','FIRE'}
class IDLE:
    @staticmethod
    def enter(self, event):
        self.dir = 0
        self.dirud = 0
        self.timer = 1000
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
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
        self.image.clip_draw(78 + int(self.frame) * 25, 187, 25, 25, self.x, self.y, 40, 40)

        # test
        # self.image.clip_draw(363 + int(self.frame) , 185, 30, 30, self.x - 2, self.y, 40, 40)

class RUN:
    def enter(self, event):
        # print("RUN ENTER")
        if event == RD:
            self.dir += 1
        elif event == RU:
            self.dir -= 1
        if event == LD:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

        if event == UD:
            self.dirud += 1
        elif event == UU:
            self.dirud -= 1
        if event == DD:
            self.dirud -= 1
        elif event == DU:
            self.dirud += 1
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.dirud * RUN_SPEED_PPS * game_framework.frame_time
        # self.x += self.x_v * game_framework.frame_time
        # self.y += self.y_v * game_framework.frame_time

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
        if self.dir == 1 or self.dir == -1:
            if self.dir == 1:
                self.right.clip_draw(7 + int(self.frame) * 24, 0, 25, 25, self.x, self.y, 40, 40)
            else:
                self.image.clip_draw(77 + int(self.frame) * 25, 160, 25, 25, self.x, self.y, 40, 40)
        elif self.dirud == 1 or self.dirud == -1:
            if self.dirud == 1:
                self.image.clip_draw(78 + int(self.frame) * 25, 80, 25, 25, self.x, self.y, 40, 40)
            else:
                self.image.clip_draw(78 + int(self.frame) * 25, 187, 25, 25, self.x, self.y, 40, 40)

        # if self.dir == 1:
        #     self.right.clip_draw(7 + int(self.frame) * 24, 0, 25, 25, self.x, self.y, 40, 40)
        # elif self.dir == -1:
        #     self.image.clip_draw(77 + int(self.frame) * 25, 160, 25, 25, self.x, self.y, 40, 40)
        # elif self.dirud == 1:
        #     self.image.clip_draw(78 + int(self.frame) * 25, 80, 25, 25, self.x, self.y, 40, 40)
        # elif self.dirud == -1:
        #     self.image.clip_draw(78 + int(self.frame) * 25, 187, 25, 25, self.x, self.y, 40, 40)
        pass

class HURT:
    def enter(self, event):
        print('HURT enter')
        self.timer = 1000
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.timer -= 5
        if self.timer == 0:
            self.cur_state = IDLE
        pass
    def exit(self, event):
        print('HURT exit')

    def draw(self):
        self.image.clip_draw(363 + int(self.frame) , 185, 30, 30, self.x - 2, self.y, 40, 40)
        pass

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
        self.image.clip_draw(430 + int(self.frame) * 30, 190, 28, 28, self.x-2, self.y-2,43,43)
        pass

next_state = {
SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, UU: RUN, DD: RUN, DU: RUN, TIMER:SLEEP, SPACE:SLEEP},
IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, UU: RUN, DD: RUN, DU: RUN, TIMER:SLEEP, SPACE:IDLE},
RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE, TIMER:RUN, SPACE:RUN},
    HURT: {RU: HURT, LU: HURT, RD: HURT, LD: HURT, UD: HURT, UU: HURT, DD: HURT, DU: HURT, TIMER:HURT, SPACE:HURT}
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.3
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
        self.frame = 0

        # 캐릭터의 체력과 번개조각 수집개수 저장
        self.hp = 500
        self.piece = 0

        self.image = load_image('img/character_eevee.png')
        self.right = load_image('img/character_eevee_right.png')
        self.light_image = load_image('img/light_piece.png')

        # 이브이의 타입 저장
        self.name = 'EVE'


        self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
    def update(self):
        global eevee_ui
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

        if self.piece == 3:
            game_framework.change_state(boss_state)
        if self.hp == 0:
            game_framework.change_state(title_state)
            self.hp = 500


        # eevee_ui.get_info(None, self.x, self.y, self.hp, self.light)
        # if Light.count == 3:
        #     game_framework.change_state(boss_state)

    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())
        # self.font.draw(self.x -10, self.y +20,'eve(hp:%3d)' %self.hp, (0,0,0) )

    def fire_ball(self):
        print('FIRE BALL')
        if self.dir == 1 or self.dir == -1:
            ball = Ball(self.x, self.y, self.face_dir,'dir')
            game_world.add_object(ball, 1)
            game_world.add_collision_pairs(None, ball, 'mob:ball')
        elif self.dirud == 1 or self.dirud == -1:
            ball = Ball(self.x, self.y, self.face_dirud,'dirud')
            game_world.add_object(ball, 1)
            game_world.add_collision_pairs(None, ball, 'mob:ball')

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
    def handle_collision(self, other, group):
        if group == "eve:piece":
            self.piece += 1
            game_world.remove_object(other)
            print('piece = ', self.piece)
        elif group == "eve:water":
            self.cur_state = HURT
           # self.q.insert(0, HD)
            self.hp -= 50
            print('eve hp = ', self.hp)
            game_world.remove_object(other)

        pass
