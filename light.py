from pico2d import *
import random
import game_world
import game_framework
import boss_state
class Light:
    count = None
    image = None
    def __init__(self, x=200, y=200, count=0):
        if Light.image == None:
            Light.image = load_image('img/light_piece.png')

        self.x, self.y, Light.count = random.randint(300,600), random.randint(300,500), 0
        pass

    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(0,0,300,300,self.x,self.y,25,25)
        draw_rectangle(*self.get_bb())
        if Light.count == 0:
            pass
        elif Light.count == 1:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
        elif Light.count == 2:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 530, 570, 40, 40)
        elif Light.count == 3:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 530, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 560, 570, 40, 40)


    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15
    def handle_collision(self, other, group):
        pass

        # elif self.count == 2:
        #     return 2
        # elif self.count == 3:
        #     return 3

