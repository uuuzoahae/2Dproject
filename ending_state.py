from pico2d import *
import game_framework
import play_state
import title_state

end_image = None
end_time = None

def enter():
    global end_image, end_time
    end_time = 0.0
    end_image = load_image('img/game_over_icon.jpg')
    pass

def exit():
    global end_image
    del end_image
    pass

def update():
    global end_time
    if end_time > 1.0:
        end_time = 0
        game_framework.change_state(title_state)
    end_time += 0.01
    delay(0.01)
    pass

def draw():
    clear_canvas()
    end_image.draw(300,300,600,600)
    update_canvas()

def handle_events():
    events = get_events()
    # for event in events:
    #     if event.type == SDL_QUIT:
    #         game_framework.quit()
    #     elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
    #         game_framework.change_state(play_state)
    #     elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
    #         game_framework.quit()

def pause():
    pass
def resume():
    pass