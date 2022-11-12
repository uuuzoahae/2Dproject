from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 300, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('fire_attack.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        self.y += self.velocity
        if self.x < 25 or self.x > 600 - 25 or self.y < 25 or self.y > 600 - 25:
            game_world.remove_object(self)
        # if self.x < 50 or self.x > 750:
        #     gameworld.remove_object(self)