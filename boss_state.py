from pico2d import *
import game_framework

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
    pass