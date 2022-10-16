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
        self.right = load_image('character_eevee_right.png')
    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir * 5
        self.y += self.dirud * 5

    def draw(self):

        # 상하
        if self.dir == 0 and self.dirud > 0:
            self.image.clip_draw(78 + self.frame * 25, 80, 25, 25, self.x, self.y, 40, 40)

        # 정지 또는 걷기
        elif self.dir == 0:
            self.image.clip_draw(78 + self.frame * 25, 187, 25, 25, self.x, self.y, 40, 40)
        elif self.dir > 0:
            self.right.clip_draw(7 + self.frame * 24, 0, 25, 25, self.x, self.y, 40, 40)
        elif self.dir < 0:
            self.image.clip_draw(77 + self.frame * 25, 160, 25, 25, self.x, self.y, 40, 40)


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

    for water in many_water:
        water.draw()
    eve.update()
    for water in many_water:
        water.update()

    delay(0.1)
    update_canvas()
    if x < 0:
        running = False
    elif x > 800:
        running = False
    elif y < 0:
        running = False
    elif y > 600:
        running = False



close_canvas()