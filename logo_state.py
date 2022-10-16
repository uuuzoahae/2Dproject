from pico2d import *
import game_framework
import title_state

running = None
logo_image = None
logo_time = None

def enter():
    global logo_image, running, logo_time
    running = True
    logo_time = 0.0
    logo_image = load_image('logo.jpg')
    pass

def update():
    global running, logo_time
    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    logo_time += 0.01
    delay(0.01)
    pass

def draw():
    clear_canvas()
    logo_image.draw(300,300,600,600)
    update_canvas()
    pass

def exit():
    global logo_image
    del logo_image
    pass

def handle_events():
    events = get_events()
    pass

# open_canvas(600,600)
#
# enter()
#
# while running:
#     handle_events()
#     update()
#     draw()
#
# exit()
#
# close_canvas()