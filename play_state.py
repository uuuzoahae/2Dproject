import random
import eevee
from pico2d import *
import game_framework
from eevee import Eve
from map import Map
from light import Light
from fire_ball import Ball
from water_drop import Water_drop
from mob import Mob
import game_world
import title_state
import boss_state
import time
frame_time = 0.0

map = None
eve = None
water = None
many_water = None
mob = None
many_mob = None
Balls = None

# def water_fall()
# #     global water, many_water
# #     many_water = [water_drop() for i in range(30)]
# #     for water in many_water:
# #         water.update()
# #     for water in many_water:
# #         water.draw()
def enter():
    global map, eve, many_water, many_mob, water, frame_time
    many_mob = [Mob() for i in range(8)]
    map = Map()
    eve = Eve()
    # water = Water_drop()
    # many_water = [Water_drop() for i in range(30)]
    light = Light()

    # 게임 오브젝트 추가
    game_world.add_object(eve, 1)
    game_world.add_object(map, 0)
    # game_world.add_objects(many_water,1)
    # game_world.add_objects(many_mob, 1)
    game_world.add_object(light,1)
    # 게임 충돌처리 추가
    game_world.add_collision_pairs(eve, many_water, 'eve:water')
    game_world.add_collision_pairs(many_mob, None, 'mob:ball')

    game_world.add_collision_pairs(eve, light, 'eve:light')


def exit():
    game_world.clear()
def update():
    for game_object in game_world.all_objects():
        game_object.update()


    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('collision', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    # global eve, many_water, water, mob, many_mob
    # eve.update()
    # # for water in many_water:
    # #     water.update()
    # for mob in many_mob:
    #     mob.update()
    # mob.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()



    # clear_canvas()
    # map.draw()
    # eve.draw()
    # # for water in many_water:
    # #     water.draw()
    # for mob in many_mob:
    #     mob.draw()
    # update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0 ):
            game_framework.change_state(boss_state)
        else:
            eve.handle_event(event)
    delay(0.1)
def pause():
    pass

def resume():
    pass

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ba > tb: return False
    if ta < bb: return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
