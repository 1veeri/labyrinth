from entities.sprite import Sprite


class Wall:
    def __init__(self, x, y, w, h, img_path):
        self.sprite = Sprite(x, y, w, h, img_path)
