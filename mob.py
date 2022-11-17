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
        # dir = random.randint(0, 3)
        # size = 20
        # if dir == 0:  # from left
        #     x = self.rect.left() - size
        #     y = random.randint(self.rect.top(), self.rect.bottom() - size)
        # elif dir == 1:  # from top
        #     x = random.randint(self.rect.left(), self.rect.right() - size)
        #     y = self.rect.top() - size
        # elif dir == 2:  # from right
        #     x = self.rect.right()
        #     y = random.randint(self.rect.top(), self.rect.bottom() - size)
        # else:  # from bottom
        #     x = random.randint(self.rect.left(), self.rect.right() - size)
        #     y = self.rect.bottom()
        self.frame = (self.frame + 1) % 2
        # self.dir = random.randint(0,1)
        # self.x += self.dir * 5
        pass
    def draw(self):
        self.image.clip_draw(self.frame*32, 25, 32, 32, self.x, self.y)
        pass

class RUN:
    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
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
        if Mob.image == None:
            Mob.image = load_image('magikarp.png')

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
            game_world.remove_object(self)
        pass