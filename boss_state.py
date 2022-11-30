from pico2d import *
import game_framework
import random
import light
from water_eevee import Water_Eve
from boss_map import Boss_Map
from light_eevee import Light_Eve
from water_drop import Water_drop
import game_world
import play_state
import time

frame_time = 0.0

eve = None
water = None
many_water = None
mob = None
many_mob = None
boss_map = None
water_eve = None
light_eve = None
random_eve = None
def enter():
    global boss_map, eve, many_water, water, frame_time, water_eve, light_eve, random_eve
    boss_map = Boss_Map()
    water_eve = Water_Eve()
    light_eve = Light_Eve()

    random_eve = random.choice([water_eve, light_eve])

    print('random_eve =  ', type(random_eve))

    # 게임 오브젝트 추가
    if random_eve.name == 'WATER':
        game_world.add_object(water_eve,1)
    elif random_eve.name == 'LIGHT':
        game_world.add_object(light_eve,1)
    game_world.add_object(boss_map, 0)

    # 게임 충돌처리 추가
    # game_world.add_collision_pairs(water_eve, many_water, 'water_eve:water')

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

# def test_self():
#     import play_state
#
#     pico2d.open_canvas()
#     game_framework.run(play_state)
#     pico2d.clear_canvas()
#
# if __name__ == '__main__':
#     test_self()

def handle_events():
    global random_eve

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_0 ):
            game_framework.change_state(play_state)
        else:
            random_eve.handle_event(event)
    pass