from pico2d import *
import random
import game_framework
import game_world
import light
import random

# 공격 받을 때, 공격이 끝났을 때를 표현하기 위한 이벤트
HIT, HIT_END = range(2)

# piece_item = None
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
        global light

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        self.timer -= 5

        # DIED 상태에서 일정시간이 흐르면 몹 삭제
        if self.timer < 0:
            print('remove mob')
            game_world.remove_object(self)

            # 랜덤한 확률로 아이템 드랍
            if random.randint(0,2) == 0:
                self.drop_piece()
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
        self.x, self.y = random.randint(50,550), random.randint(50,550)
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

        # 맵에 몹이 죽을때마다, 리스폰
        if self.count_mob() <= 6:
            self.add_mobs()
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
        # draw_rectangle(*self.get_bb())
        pass
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15
    def handle_collision(self, other, group):
        if group == 'mob:ball':
            self.event_q.insert(0, HIT)

    # 아이템 (번개조각) 드랍하는 함수 생성
    def drop_piece(self):
        piece_item = light.Piece(self.x, self.y)
        game_world.add_object(piece_item, 1)
        game_world.add_collision_pairs(None,piece_item,'eve:piece')

    def count_mob(self): # 월드에 존재하는 몹의 개체수 카운트
        num = 0
        for game_object in game_world.all_objects():
            if isinstance(game_object, Mob):
                num += 1
        return num

    def add_mobs(self): # 랜덤 리스폰 함수
        c = random.randint(0,3) # 랜덤 개체수
        new_mobs = [Mob() for i in range(c)]
        game_world.add_objects(new_mobs, 1)
        game_world.add_collision_pairs(new_mobs,None,'mob:ball')

