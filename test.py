import random
from pico2d import *

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
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dirud += 1
            elif event.key == SDLK_DOWN:
                dirud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dirud -= 1
            elif event.key == SDLK_DOWN:
                dirud += 1

running = True

x = 800 / 2
y = 600 / 2
frame = 0
dir = 0
dirud = 0


open_canvas(600,600)
map = load_image('main_map.png')
eve = load_image('character_eevee.png')

many_water = [water_drop() for i in range(30)]

while running:
    clear_canvas()
    map.draw(300, 300, 600, 600)

    handle_events()

    for water in many_water:
        water.update()

    for water in many_water:
        water.draw()

    # 정지
    if dir == 0:
        eve.clip_draw(frame * 20, 190, 25 , 25, x, y, 40, 40)
        frame = (frame + 1) % 2

    # 걷기
    elif dir > 0:
        eve.clip_draw(80 + frame * 24, 190, 25, 25, x, y, 40, 40)
        frame = (frame + 1) % 3

    elif dir < 0:
        eve.clip_draw(70 + frame * 28, 160, 25, 25, x, y, 40, 40)
        frame = (frame + 1) % 3

    update_canvas()


    if x < 0:
        running = False
    elif x > 800:
        running = False
    elif y < 0:
        running = False
    elif y > 600:
        running = False

    y += dirud * 10
    x += dir * 10

    delay(0.1)

