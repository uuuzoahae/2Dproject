import random
from pico2d import *

class Map():
    def __init__(self):
        self.image = load_image('main_map.png')
    def draw(self):
        self.image.draw(300,300,600,600)
class eevee():
    def __init__(self):
        self.x,self.y = 400, 300
        self.dir = 0
        self.dirud = 0
        self.frame = 0
        self.image = load_image('character_eevee.png')
    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir * 1
        self.y += self.dirud * 1
    def draw(self):
        # 정지
        if self.dir == 0:
            self.image.clip_draw(self.frame * 20, 190, 25, 25, self.x, self.y, 40, 40)
        # 걷기
        elif self.dir > 0:
            self.image.clip_draw(80 + self.frame * 24, 190, 25, 25, self.x, self.y, 40, 40)
        elif self.dir < 0:
            self.image.clip_draw(70 + self.frame * 28, 160, 25, 25, self.x, self.y, 40, 40)

class water_drop():
    def __init__(self):
        self.x, self.y = random.randint(0 ,700) , random.randint(300 ,600)
        self.image = load_image('water_drop.png')
    def update(self):
        if self.y >= -300:
            self.y -= 5
    def draw(self):
        self.image.clip_draw(0, 0, 1000, 1000, self.x, self.y, 50, 50)

def handle_events():
    global running
    global x, y
    global dir, dirud

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                eve.dir += 1
            elif event.key == SDLK_LEFT:
                eve.dir -= 1
            elif event.key == SDLK_UP:
                eve.dirud += 1
            elif event.key == SDLK_DOWN:
                eve.dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                eve.dir -= 1
            elif event.key == SDLK_LEFT:
                eve.dir += 1
            elif event.key == SDLK_UP:
                eve.dirud -= 1
            elif event.key == SDLK_DOWN:
                eve.dirud += 1

running = True

x = 800 / 2
y = 600 / 2
frame = 0
dir = 0
dirud = 0


open_canvas(600,600)
map = Map()
eve = eevee()

many_water = [water_drop() for i in range(30)]

while running:
    handle_events()
    clear_canvas()
    map.draw()
    eve.draw()
    eve.update()
    update_canvas()
    for water in many_water:
        water.draw()
    for water in many_water:
        water.update()
    if x < 0:
        running = False
    elif x > 800:
        running = False
    elif y < 0:
        running = False
    elif y > 600:
        running = False



close_canvas()