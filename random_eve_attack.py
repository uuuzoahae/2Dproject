from pico2d import *
import game_world

class Ev_Ball:
    image = None

    def __init__(self, x , y , velocity, direction):
        if Ev_Ball.image == None:
            Ev_Ball.image = load_image('img/pink_fire2.png')
        self.x, self.y, self.velocity, self.direction= x, y, velocity, direction

    def draw(self):
        self.image.draw(self.x, self.y)
        # draw_rectangle(*self.get_bb())

    def update(self):
        if self.direction == 'dir':
            self.x += self.velocity * 1
            # if self.x < 25 or self.x > 600 - 25 or self.y < 25 or self.y > 600 - 25:
            #     game_world.remove_object(self)
        elif self.direction == 'dirud':
            self.y += self.velocity * 1

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        pass