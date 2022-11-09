from pico2d import *
import game_framework

boss_map = None
running = None

def enter():
    global running, boss_map
    running = True
    boss_map = load_image('boss_map.png')
    pass

def exit():
    pass

def draw():
    clear_canvas()
    boss_map.draw(300,300,600,600)
    update_canvas()
    pass

def update():
    pass

def handle_events():
    events = get_events()
    pass