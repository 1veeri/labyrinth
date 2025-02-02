from pygame import Rect
from pygame.image import load
from pygame.transform import scale


class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.hitbox = Rect(x, y, w, h)
        self.img = scale(load(img_path), (w, h))

    def draw(self, screen):
        screen.blit(self.img, self.hitbox)
