import pico2d
import game_framework

import logo_state

pico2d.open_canvas(600,600)
game_framework.run(logo_state)
pico2d.close_canvas()