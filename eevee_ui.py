from pico2d import *
import game_framework
class UI:
    image = None
    light_image = None
    def __init__(self, x, y, hp, piece):
        if UI.image == None:
            UI.image = load_image('img/heart.png')
        if UI.light_image == None:
            UI.light_image = load_image('img/yellow_heart.png')

        self.frame = 0
        self.x = x
        self.y = y
        self.hp = hp
        self.piece = piece
        # self.font = load_font('font/PKMN-Mystery-Dungeon.ttf',20)

    # def get_info(self, x, y, hp, light):
    #     self.x = x, self.y = y
    #     self.hp = hp, self.light = light

    def draw(self):

        # hp ui
        if self.hp <= 300 and self.hp > 200:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x + 18, self.y+25,22,22)
        elif self.hp <= 200 and self.hp > 100:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)
            self.image.clip_draw(int(self.frame),0,100,100,self.x , self.y+25,22,22)
        elif self.hp <= 100 and self.hp > 0:
            self.image.clip_draw(int(self.frame),0,100,100,self.x - 18, self.y+25,22,22)

        # light piece 아이템 ui
        if self.piece == 1:
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x - 18, self.y - 25, 22, 22)
        elif self.piece == 2:
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x - 18, self.y - 25, 22, 22)
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x , self.y - 25, 22, 22)
        elif self.piece == 3:
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x - 18, self.y - 25, 22, 22)
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x , self.y - 25, 22, 22)
            self.light_image.clip_draw(int(self.frame), 0, 100, 100, self.x + 18, self.y - 25, 22, 22)



        # self.hp_image.draw(300,300,300,300)
        pass

    def update(self):
        self.frame += game_framework.frame_time
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