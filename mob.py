from pico2d import *
import random
import game_world
class IDLE:
    def enter(self):
        print('Mob Enter')
        pass
    def exit(self):
        pass
    def do(self):
        self.frame = (self.frame + 1) % 2
        pass
    def draw(self):
        self.image.clip_draw(self.frame*32, 25, 32, 32, self.x, self.y)
        pass

class ATTACKED:
    def enter(self):
        self.hp = 5000
        print("attcked enter")

    def exit(self):
        print("attacked exit")
        pass

    def do(self):
        self.frame = (self.frame + 1) % 2
        self.hp -= 50
        if self.hp == 0:
            self.cur_state.exit(self)
            self.cur_state = DIED
            self.cur_state.enter(self)
        pass

    def draw(self):
        self.image.clip_draw(80 + self.frame * 46, 27, 32, 32, self.x, self.y)
        pass
class DIED:
    def enter(self):
        print("DIEDDIED ENTER")

    def exit(self):
        print("DIEDDIED EXIT")
        pass

    def do(self):
        print("DIED DO")
        pass

    def draw(self):
        pass
# next_state = {
# IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UD: RUN, UU: RUN, DD: RUN, DU: RUN},
# RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE}
# }
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
            self.cur_state.exit(self)
            self.cur_state = ATTACKED
            self.cur_state.enter(self)
            self.cur_state.do(self)
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