import random
from pico2d import *

class Water_drop():
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0 ,700) , random.randint(300 ,600)
        # self.image = load_image('water_drop.png')
        if Water_drop.image == None:
            Water_drop.image = load_image('water_drop.png')
    def update(self):
        if self.y >= -300:
            self.y -= 5
        self.x -= random.randint(-5,5)
    def draw(self):
        self.image.clip_draw(0, 0, 1000, 1000, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-10, self.y-10, self.x+10, self.y+10
