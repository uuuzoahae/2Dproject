from pico2d import *
import random
import eevee
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
import play_state
import time
frame_time = 0.0

map = None
eve = None
water = None
many_water = None
mob = None
many_mob = None
Balls = None
count = 0


class Map():
    def __init__(self):
        self.image = load_image('boss_map.png')
    def draw(self):
        self.image.draw(300,300,600,600)


boss_map = None
running = None

def enter():
    global running, boss_map
    running = True
    boss_map = Map()
    pass

def exit():
    global boss_map
    del boss_map
    pass

def draw():
    clear_canvas()
    boss_map.draw()
    update_canvas()
    pass

def update():
    pass

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