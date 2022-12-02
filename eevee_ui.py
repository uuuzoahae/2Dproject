from pico2d import *
class UI:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 500
        self.light = 0
        self.light_image = load_image('img/light_piece.png')
        self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

    # def get_info(self, x, y, hp, light):
    #     self.x = x, self.y = y
    #     self.hp = hp, self.light = light

    def draw(self):
        # self.hp_image.draw(300,300,300,300)
        pass

    def update(self):
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