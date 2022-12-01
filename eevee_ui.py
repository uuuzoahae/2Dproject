from pico2d import *
import eevee

class UI:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = 500
        self.light = 0
        self.hp_image = load_image('img/hp_bar.png')
        self.light_image = load_image('img/light_piece.png')
        self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

    # def get_info(self, x, y, hp, light):
    #     self.x = x, self.y = y
    #     self.hp = hp, self.light = light

    def draw(self):
        pass

    def update(self):
        self.x, self.y, self.hp, self.light = eevee.get_info()
        # print('eve ui = x, y, hp, light ', self.x, self.y, self.hp, self.light)
        pass

    def handle_event(self):
        pass

    def play_sound(self):
        pass