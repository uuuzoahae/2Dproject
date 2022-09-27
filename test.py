from pico2d import *

open_canvas()
clear_canvas()

map = load_image('map.png')
eevee = load_image('eve.png')


map.draw(400,300,800,800)
eevee.draw(400,300,100,100)

update_canvas()

delay(10)