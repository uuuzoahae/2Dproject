from pico2d import *
import random
import game_framework
import game_world

# 공격 받을 때, 공격이 끝났을 때를 표현하기 위한 이벤트
HIT, HIT_END = range(2)

class IDLE:
    def enter(self,event):
        self.timer = 1000
        pass
    def exit(self):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pass
    def draw(self):
        self.image.clip_draw(int(self.frame) * 32, 25, 32, 32, self.x, self.y)
        pass

class ATTACKED:
    def enter(self,event):
        self.hp -= 5
        pass

    def exit(self):
        self.event_q.insert(0,HIT_END)
        pass


    def do(self):
        self.frame = (self.frame + 0.1 * ACTION_PER_TIME * game_framework.frame_time) % 2
        if self.hp == 0:
            self.cur_state = DIED

    def draw(self):
        self.image.clip_draw(80 + int(self.frame) * 46, 27, 32, 32, self.x, self.y)
        pass
class DIED:
    def enter(self,event):
        pass

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        self.timer -= 5

        # DIED 상태에서 일정시간이 흐르면 몹 삭제

        if self.timer < 0:
            print('remove mob')
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.clip_draw(170 + int(self.frame) * 46, 27, 32, 32, self.x, self.y)
        pass

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

next_state = {
ATTACKED: {HIT:ATTACKED, HIT_END: IDLE},
IDLE: {HIT:ATTACKED, HIT_END:IDLE},
DIED: {HIT:DIED, HIT_END:DIED}
}
class Mob():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(20,580), random.randint(20,600)
        self.dir = 0
        self.frame = 0
        self.hp = 500
        if Mob.image == None:
            Mob.image = load_image('img/magikarp.png')

        self.event_q = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)
        pass

    def update(self):
        self.cur_state.do(self)
        if self.event_q:
            event = self.event_q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, None)
        pass

    def add_event(self, event):
        self.event_q.insert(0, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def handle_collision(self, other, group):
        if group == 'mob:ball':
            self.event_q.insert(0, HIT)