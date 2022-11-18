from pico2d import *
import random
import game_world
import game_framework
import boss_state
class Light:
    num = None
    image = None
    def __init__(self, x=200, y=200, count=0):
        if Light.image == None:
            Light.image = load_image('light_piece.png')

        self.x, self.y, Light.num = random.randint(300,600), random.randint(300,500), 0
        pass

    def update(self):
        if Light.num == 3:
            game_framework.change_state(boss_state)
        pass

    # def draw_light(self, light_num):

    def draw(self):
        self.image.clip_draw(0,0,300,300,self.x,self.y,25,25)
        draw_rectangle(*self.get_bb())
        if Light.num == 0:
            pass
        elif Light.num == 1:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
        elif Light.num == 2:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 530, 570, 40, 40)
        elif Light.num == 3:
            Light.image.clip_draw(0, 0, 300, 300, 500, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 530, 570, 40, 40)
            Light.image.clip_draw(0, 0, 300, 300, 560, 570, 40, 40)


    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15
    def handle_collision(self, other, group):
        if group == "eve:light":
            Light.num += 1
            print(" ",Light.num)
            game_world.remove_object(self)

        # elif self.count == 2:
        #     return 2
        # elif self.count == 3:
        #     return 3

