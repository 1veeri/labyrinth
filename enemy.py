from sprite import Sprite


class Enemy:
    def __init__(self, x, y, w, h, img_path, speed):
        self.sprite = Sprite(x, y, w, h, img_path)
        self.speed = speed

    def move(self, walls):
        self.sprite.hitbox.x += self.speed
        for wall in walls:
            if self.sprite.hitbox.colliderect(wall.sprite.hitbox):
                self.speed *= -1
