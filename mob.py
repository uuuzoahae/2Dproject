class IDLE:
    def enter(self):
        pass
    def exit(self):
        pass
    def do(self):
        pass
    def draw(self):
        pass

class RUN:
    def enter(self):
        pass

    def exit(self):
        pass

    def do(self):
        pass

    def draw(self):
        pass

class Mob():
    def __init__(self):
        self.x, self.y = 300, 300
        self.dir = 0
        self.dirud = 0
        self.frame = 0
        self.image = load_image('character_eevee.png')
        self.right = load_image('character_eevee_right.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)
        pass

    def update(self):
        self.cur_state.do(self)
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        pass