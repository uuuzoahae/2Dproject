from pico2d import *
import random

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

eve = eevee()

open_canvas(600,600)

while running:
    handle_events()
    clear_canvas()
    map.draw()
    eve.draw()
    eve.update()
    update_canvas()

    for water in many_water:
        water.update()
    for water in many_water:
        water.draw()


    if x < 0:
        running = False
    elif x > 800:
        running = False
    elif y < 0:
        running = False
    elif y > 600:
        running = False

    delay(0.01)

close_canvas()