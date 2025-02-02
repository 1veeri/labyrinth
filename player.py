from sprite import Sprite


class Player:
    def __init__(self, x, y, w, h, img_path, speed):
        self.sprite = Sprite(x, y, w, h, img_path)
        self.speed = [0, 0]
        self.maxspeed = speed
    def move(self, walls):
        self.sprite.hitbox.x += self.speed[0]
        for wall in walls:
            if self.sprite.hitbox.colliderect(wall.sprite.hitbox):
                self.sprite.hitbox.x -= self.speed[0]
        self.sprite.hitbox.y += self.speed[1]
        for wall in walls:
            if self.sprite.hitbox.colliderect(wall.sprite.hitbox):
                self.sprite.hitbox.y -= self.speed[1]
        