from pico2d import *
import random

class water_drop():
    def __init__(self):
        self.x,self.y = random.randint(0,700),random.randint(300,600)
        self.image = load_image('water_drop.png')
    def update(self):
        if self.y >= -300:
            self.y -= 5
    def draw(self):
        self.image.clip_draw(0,0,1000,1000,self.x,self.y,50,50)

def handle_events():
    global running
    global x, y
    global dir, dirud

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT and SDL_KEYDOWN:
            running = False
        elif event.key == SDLK_ESCAPE:
            running = False


x = 400
y = 300
running = True

open_canvas()

many_water = [water_drop() for i in range(20)]

while running:
    handle_events()
    clear_canvas()

    for water in many_water:
        water.update()

    for water in many_water:
        water.draw()

    update_canvas()

    delay(1)