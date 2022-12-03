from pico2d import *
import random
import game_framework
import game_world
class IDLE:
    def enter(self):
        print('Mob Enter')
        self.timer = 1000
        pass
    def exit(self):
        pass
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        pass
    def draw(self):
        self.image.clip_draw(int(self.frame) * 32, 25, 32, 32, self.x, self.y) #IDLE
        pass

class ATTACKED:
    def enter(self):
        print("attcked enter")

    def exit(self):
        print("attacked exit")
        # self.cur_state.exit(self)
        # self.cur_state = DIED
        # self.cur_state.enter(self)
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.hp -= 5
        if self.hp < 0:
            self.cur_state = DIED
        pass

    def draw(self):
        self.image.clip_draw(80 + int(self.frame) * 46, 27, 32, 32, self.x, self.y)
        pass
class DIED:
    def enter(self):
        print("DIEDDIED ENTER")

    def exit(self):
        print("DIEDDIED EXIT")
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1
        # print("DIED")
        self.timer -= 5
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

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 3
class Mob():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(20,580), random.randint(20,600)
        self.dir = 0
        self.frame = 0
        self.hp = 500
        if Mob.image == None:
            Mob.image = load_image('img/magikarp.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self)
        pass

    def update(self):
        self.cur_state.do(self)

        # if self.q:
        #     event = self.q.pop()
        #     self.cur_state.exit(self)
        #     self.cur_state = next_state[self.cur_state][event]
        #     self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def handle_collision(self, other, group):
        if group == 'mob:ball':
            self.cur_state = ATTACKED
            print('mob hp = ',self.hp )

        # if group == 'mob:ball':
        #     game_world.remove_object(self)
        pass

    # def fire_ball(self):
    #     print('FIRE BALL')
    #
    #     if self.dir == 1 or self.dir == -1:
    #         ball = Ball(self.x, self.y, self.face_dir)
    #         game_world.add_object(ball, 1)
    #         game_world.add_collision_pairs(None, ball, 'mob:ball')