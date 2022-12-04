import random
import math
import game_framework
import winsound
import ending_state

from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf
from pico2d import *
import game_world

# import server
# from ball import Ball

import boss_state

#
class TargetMarker:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        # self.image = load_image('hand_arrow.png')
    def update(self):
        pass
    def draw(self):
        pass
        # self.image.draw(self.x, self.y, 50, 50)














# gyarados speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# gyarados action speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10





# animation_names = ['Attack', 'Died', 'Hurt', 'Idle','Special Attack','Walk' ]
animation_names = ['Idle', 'Walk']

class Gyarados:
    images = None

    def load_images(self):
        if Gyarados.images == None:
            Gyarados.images = {}
            Gyarados.images['Idle'] = [load_image("boss/gayarados/" + 'Idle' + " (%d)" % i + ".png") for i in range(1,3)]
            Gyarados.images['Walk'] = [load_image("boss/gayarados/" + 'Walk' + " (%d)" % i + ".png") for i in range(1,5)]

    def __init__(self):
        #self.x, self.y = 1280 / 4 * 3, 1024 / 4 * 3
        self.x, self.y = random.randint(200, 600), random.randint(200, 600)
        self.tx, self.ty = random.randint(100, 550), random.randint(100, 550)
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0.0
        self.build_behavior_tree()

        # self.target_ball = None
        # self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 2000

        self.target_marker = TargetMarker(self.tx, self.ty)
        # game_world.add_object(self.target_marker, 1)


    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 500)
        self.y = clamp(50, self.y, 500)

    # def find_random_location(self):
    #     self.tx, self.ty = random.randint(50, 550), random.randint(50, 550)
    #     self.target_marker.x, self.target_marker.y = self.tx, self.ty
    #     return BehaviorTree.SUCCESS
    #     pass

    def move_to(self, radius = 0.5):
        distance = (self.tx - self.x) ** 2 + (self.ty - self.y) **2
        self.dir = math.atan2(self.ty - self.y, self.tx - self.x)

        distance = (300 -  self.x) ** 2 + (300 - self.y) **2
        self.dir = math.atan2(300 - self.y, 300 - self.x)
        if distance < (PIXEL_PER_METER * radius) ** 2:
            self.speed = 0
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING

        pass

    # def play_beep(self):
    #     winsound.Beep(440, 100)
    #     return BehaviorTree.SUCCESS

    # def find_ball_location(self):
    #     self.target_ball = None
    #     shortest_distance = 1280 ** 2
    #     # find in-sight(5meters) and nearest ball
    #     for o in game_world.all_objects():
    #         if type(o) is Ball:
    #             ball = o
    #             distance = (ball.x - self.x) **2 + (ball.y - self.y) **2
    #             if distance < (PIXEL_PER_METER * 7) **2 and distance < shortest_distance:
    #                 self.target_ball = ball
    #                 shortest_distance = distance
    #     if self.target_ball is not None:
    #         self.tx, self.ty = self.target_ball.x, self.target_ball.y
    #         return BehaviorTree.SUCCESS
    #     else:
    #         return BehaviorTree.FAIL
    #     pass

    def calculate_squared_distance(self, a, b):
        # print(' ', a.x, b.x, a.y, b.y)
        return (a.x-b.x)**2 + (a.y-b.y)**2

    def move_to_boy(self):
        distance = self.calculate_squared_distance(self, boss_state.random_eve)

        if distance > (PIXEL_PER_METER * 5) ** 2:
            self.speed = 0
            # print('behavior fail')
            return BehaviorTree.FAIL

        if distance < (PIXEL_PER_METER * 0.1) ** 2:
            self.speed = 0
            print('mov to success')
            return BehaviorTree.SUCCESS
        else:
            self.speed = RUN_SPEED_PPS
            return BehaviorTree.RUNNING

        #
        # else:
        #     self.speed = 0
        #     return BehaviorTree.FAIL


        # if distance > (PIXEL_PER_METER * 10) ** 2:
        #     self.speed = 0
        #     return BehaviorTree.FAIL
        # if self.hp > boss_state.random_eve.hp:
        #     self.dir = math.atan2(server.boy.y - self.y, server.boy.x - self.x)
        #     if distance < (PIXEL_PER_METER * 0.5) ** 2:
        #         self.speed = 0
        #         return BehaviorTree.SUCCESS
        #     else:
        #         self.speed = RUN_SPEED_PPS
        #         return BehaviorTree.RUNNING
        # else:
        #     self.speed = 0
        #     return BehaviorTree.FAIL

    # def flee_from_boy(self):
    #     distance = self.calculate_squared_distance(self, server.boy)
    #     if distance > (PIXEL_PER_METER * 10) ** 2:
    #         self.speed = 0
    #         return BehaviorTree.FAIL
    #     if self.hp <= server.boy.hp:
    #         self.dir = math.atan2(self.y - server.boy.y, self.x - server.boy.x)
    #         self.speed = RUN_SPEED_PPS
    #         return BehaviorTree.RUNNING
    #     else:
    #         self.speed = 0
    #         return BehaviorTree.FAIL

    def build_behavior_tree(self):
        # find_random_location_node = Leaf('Find Random Location', self.find_random_location)
        # move_to_node = Leaf('Move To', self.move_to)
        # play_beep_node = Leaf('Play Beep', self.play_beep)
        # wander_sequence = Sequence('Wander', find_random_location_node,move_to_node)

        # find_ball_location_node = Leaf('Find Ball Location', self.find_ball_location)
        # eat_ball_sequence = Sequence('Eat Ball', find_ball_location_node, move_to_node, play_beep_node)
        #
        # wander_or_eat_ball_selector = Selector('Wander or Eat Ball', eat_ball_sequence, wander_sequence)
        #
        move_to_boy_node = Leaf('Move to Boy', self.move_to_boy)
        # flee_from_boy_node = Leaf('Flee from Boy', self.flee_from_boy)
        # chase_or_flee_selector = Selector('Chase or Flee Boy', move_to_boy_node, flee_from_boy_node)

        # final_selector = Selector('Final', chase_or_flee_selector, wander_or_eat_ball_selector)
        # self.bt = BehaviorTree(final_selector)



        self.bt = BehaviorTree(move_to_boy_node)
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()
        self.calculate_current_position()
        if self.hp < 0:
            game_world.remove_object(self)
            game_framework.change_state(ending_state)


    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Gyarados.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Gyarados.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Gyarados.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Gyarados.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)
    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):
        if 'boss:ball' == group:
            self.hp -= 1
            print(' boss hp = ', self.hp)
