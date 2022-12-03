from pico2d import *
class UI:
    hp_image = None
    light_image = None
    def __init__(self):
        if self.hp_image == None:
            self.hp_image = load_image('img/heart.py')
        if self.light_image == None:
            self.light_image = load_image('img/light_piece.py')

        self.frame = 0
        self.x = 0
        self.y = 0
        self.gauge = 300
        self.inven = 0
        self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

    # def get_info(self, x, y, hp, light):
    #     self.x = x, self.y = y
    #     self.hp = hp, self.light = light

    def draw(self):
        # self.hp_image.draw(300,300,300,300)
        pass

    def update(self):
        self.get_info()
        pass

    def handle_event(self):
        pass

    def play_sound(self):
        pass

    def get_info(self, x, y, hp, light):
        self.x = x
        self.y = y
        self.hp = hp
        self.light = light