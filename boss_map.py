from pico2d import *

class Boss_Map():
    def __init__(self):
        self.image = load_image('img/boss_map.png')
    def draw(self):
        self.image.draw(300,300,600,600)

    def update(self):
        pass