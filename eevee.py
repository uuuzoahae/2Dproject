from pico2d import *

class eevee():
    def __init__(self):
        self.x,self.y = 300, 300
        self.dir = 0
        self.dirud = 0
        self.face_dir = 1
        self.frame = 0
        self.image = load_image('character_eevee.png')
        self.right = load_image('character_eevee_right.png')
    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dir * 5
        self.y += self.dirud * 5
    def draw(self):
        # 상하
        if self.dir == 0 and self.dirud > 0:
            self.image.clip_draw(78 + self.frame * 25, 80, 25, 25, self.x, self.y, 40, 40)

        # 정지 또는 걷기
        elif self.dir == 0:
            self.image.clip_draw(78 + self.frame * 25, 187, 25, 25, self.x, self.y, 40, 40)
        elif self.dir > 0:
            self.right.clip_draw(7 + self.frame * 24, 0, 25, 25, self.x, self.y, 40, 40)
        elif self.dir < 0:
            self.image.clip_draw(77 + self.frame * 25, 160, 25, 25, self.x, self.y, 40, 40)
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            match event.key:
            case pico2d.SDLK_LEFT:
            self.dir -= 1
            case pico2d.SDLK_RIGHT:
            self.dir += 1
        elif event.type == SDL_KEYUP:
            match event.key:
            case SDLK_LEFT:
            self.dir += 1
            self.face_dir = -1
            case SDLK_RIGHT:
            self.dir -= 1
            self.face_dir = 1