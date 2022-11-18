
import game_framework
import random
import eevee

from pico2d import *
from eevee import Eve
from boss_map import Boss_Map
from water_drop import Water_drop
import game_world
import boss_state
import play_state
import time

frame_time = 0.0

eve = None
water = None
many_water = None
mob = None
many_mob = None
boss_map = None


def enter():
    global map, eve, many_water, many_mob, water, frame_time, count
    boss_map = Boss_Map()
    eve = Eve()

    # 게임 오브젝트 추가
    game_world.add_object(eve, 1)
    game_world.add_object(map, 0)

    # 게임 충돌처리 추가
    game_world.add_collision_pairs(eve, many_water, 'eve:water')

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

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

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
















def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0 ):
            game_framework.change_state(play_state)
    pass