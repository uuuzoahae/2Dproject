from pico2d import *
import game_framework
import logo_state
import boss_state
import play_state
import title_state

open_canvas(600,600)
# game_framework.run(logo_state)
# game_framework.run(boss_state)
game_framework.run(title_state)
close_canvas()