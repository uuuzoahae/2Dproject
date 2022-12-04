from pico2d import *
import game_framework
class UI:
    image = None
    def __init__(self, x, y, hp):
        if UI.image == None:
            UI.image = load_image('img/heart2.png')

        self.frame = 0
        self.x = x
        self.y = y
        self.hp = hp
        # self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

    # def get_info(self, x, y, hp, light):
    #     self.x = x, self.y = y
    #     self.hp = hp, self.light = light

    def draw(self):
        # hp ui
        # self.image.clip_draw(int(self.frame), 0, 100, 100, self.x - 18, self.y + 25, 22, 22)
        if self.hp <= 300 and self.hp > 200:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x + 18, self.y+25,22,22)
        elif self.hp <= 200 and self.hp > 100:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
        elif self.hp <= 100 and self.hp > 0:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)


    def update(self):
        self.frame += game_framework.frame_time
        pass

    def handle_event(self):
        pass

    def play_sound(self):
        pass
