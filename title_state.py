from pico2d import *
import game_framework
import play_state

title_image = None

def enter():
    global title_image
    title_image = load_image('img/title.png')
    pass

def exit():
    global title_image
    del title_image
    pass

def update():
    pass

def draw():
    clear_canvas()
    title_image.draw(300,300,600,600)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
            # if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            #     game_framework.quit()
            # elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #     if events:
            #         game_framework.change_state(play_state)
            #     else:
            #         game_framework.pop_state(play_state)
def pause():
    pass
def resume():
    pass