from pico2d import *
import random
import game_world
import game_framework

class Light:
    image = None
    def __init__(self, x=200, y=200, count=0):
        if Light.image == None:
            Light.image = load_image('light_piece.png')

        self.x, self.y, self.count = x, y, 0
        pass

    def update(self):
        if self.count == 0:
            print("light piece count +0")
            # self.image.draw(500,600)
        elif self.count == 1:
            print("light piece count +1")
            # self.image.draw(500,600)
            # self.image.draw(550,600)
        elif self.count == 2:
            print("light piece count +2")
        elif self.count == 3:
            print('light piece count +3')

        pass

    def draw(self):
        self.image.clip_draw(0,0,300,300,self.x,self.y,25,25)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def handle_collision(self, other, group):
        if group == "eve:light":
            self.count += 1
            game_world.remove_object(self)
    def count_light(self):
        if self.count == 0:
            return 0
        elif self.count == 1:
            return 1
        elif self.count == 2:
            return 2
        elif self.count == 3:
            return 3

