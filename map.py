from pico2d import *
class Map():
    def __init__(self):
        self.image = load_image('main_map.png')
    def draw(self):
        self.image.draw(300,300,600,600)
