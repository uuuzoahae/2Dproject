import random
from pico2d import *
import game_framework
from eevee import Eve
from map import Map
from water_drop import Water_drop
from mob import Mob

map = None
eve = None
water = None
running = None
dir = None
face_dir = None
many_water = None
mob = None


# def water_fall():
# #     global water, many_water
# #     many_water = [water_drop() for i in range(30)]
# #     for water in many_water:
# #         water.update()
# #     for water in many_water:
# #         water.draw()
def enter():
    global map, eve, water, running, dir, face_dir, many_water, mob

    mob = Mob()
    map = Map()
    eve = Eve()
    water = Water_drop()
    many_water = [Water_drop() for i in range(30)]

    running = True
    dir = 0
    face_dir = 1

def exit():
    global map, eve, water, many_water, mob
    del map
    del eve
    del water
    del mob

def update():
    global eve, many_water, water, mob
    eve.update()
    for water in many_water:
        water.update()
    mob.update()

def draw():
    clear_canvas()
    map.draw()
    eve.draw()
    for water in many_water:
        water.draw()
    mob.draw()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            eve.handle_event(event)
    delay(0.1)



        # elif event.type == SDL_KEYDOWN:
        #     if event.key == SDLK_RIGHT:
        #         eve.dir += 1
        #     elif event.key == SDLK_LEFT:
        #         eve.dir -= 1
        #     elif event.key == SDLK_UP:
        #         eve.dirud += 1
        #     elif event.key == SDLK_DOWN:
        #         eve.dirud -= 1
        #     elif event.key == SDLK_ESCAPE:
        #         game_framework.change_state(title_state)
        # elif event.type == SDL_KEYUP:
        #     if event.key == SDLK_RIGHT:
        #         eve.dir -= 1
        #     elif event.key == SDLK_LEFT:
        #         eve.dir += 1
        #     elif event.key == SDLK_UP:
        #         eve.dirud -= 1
        #     elif event.key == SDLK_DOWN:
        #         eve.dirud += 1
        # delay(0.1)

# open_canvas(600,600)
#
#
# enter()
# while running:
#     handle_events()
#     update()
#     delay(0.1)
#     draw()
#
# exit()
#
# close_canvas()


