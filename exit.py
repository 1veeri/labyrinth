from pygame import Rect


class End:
    def __init__(self, x, y, w, h):
        self.hitbox = Rect(x, y, w, h)