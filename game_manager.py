import pygame
import settings as s
from sys import exit
from entities.player import Player
from entities.wall import Wall
from entities.enemy import Enemy
from exit import End


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((s.WIDTH_SCREEN, s.HEIGHT_SCREEN))
        self.clock = pygame.time.Clock()
        self.game_state = "start"

        self.font = pygame.font.SysFont("Bahnschrift Condensec", 40)
        self.start_text1 = self.font.render("Labyrinth", True, s.TEXT_COLOR)
        self.start_text2 = self.font.render("Start", True, s.TEXT_COLOR)
        self.end_text1 = self.font.render("You won!", True, s.TEXT_COLOR)
        self.end_text2 = self.font.render("You died..", True, s.TEXT_COLOR)
        self.end_text3 = self.font.render("Try again", True, s.TEXT_COLOR)
        self.button_rect_start = pygame.Rect(
            0, 0, self.start_text2.get_width() + 20, self.start_text2.get_height() + 20
        )
        self.button_rect_start.center = (
            s.WIDTH_SCREEN / 2,
            300 + self.start_text2.get_height() / 2,
        )
        self.button_rect_again = pygame.Rect(
            0, 0, self.end_text3.get_width() + 20, self.end_text3.get_height() + 20
        )
        self.button_rect_again.center = (
            s.WIDTH_SCREEN / 2,
            300 + self.end_text3.get_height() / 2,
        )

        self.player = None
        self.level_number = 0
        self.won = 0

        self.walls = []
        self.enemies = []
        self.ends = []
        self.switch_level()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if self.game_state == "start":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_state = "game"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect_start.collidepoint(event.pos):
                        self.game_state = "game"
            if self.game_state == "game":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.speed[1] = -self.player.maxspeed
                    if event.key == pygame.K_a:
                        self.player.speed[0] = -self.player.maxspeed
                    if event.key == pygame.K_s:
                        self.player.speed[1] = self.player.maxspeed
                    if event.key == pygame.K_d:
                        self.player.speed[0] = self.player.maxspeed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player.speed[1] = 0
                    if event.key == pygame.K_a:
                        self.player.speed[0] = 0
                    if event.key == pygame.K_s:
                        self.player.speed[1] = 0
                    if event.key == pygame.K_d:
                        self.player.speed[0] = 0
            if self.game_state == "end":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level_number = 0
                        self.switch_level()
                        self.game_state = "game"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect_again.collidepoint(event.pos):
                        self.level_number = 0
                        self.switch_level()
                        self.game_state = "game"

    def switch_level(self):
        self.level_number += 1
        if self.level_number > s.LEVEL_AMOUNT:
            self.won = 1
            self.game_state = "end"
        else:
            self.load_level(self.level_number)

    def load_level(self, level_number):
        walls = []
        enemies = []
        ends = []
        with open(rf"assets\levels\lvl{level_number}.txt") as level:
            for row, line in enumerate(level.read().splitlines()):
                for col, char in enumerate(line):
                    if char == "1":
                        walls.append(
                            Wall(col * 20, row * 20, 20, 20, r"assets\images\wall.png")
                        )
                    if char == "2":
                        enemies.append(
                            Enemy(
                                col * 20,
                                row * 20,
                                20,
                                20,
                                r"assets\images\enemy.png",
                                5,
                            )
                        )
                    if char == "3":
                        self.player = Player(
                            col * 20, row * 20, 20, 20, r"assets\images\player.png", 5
                        )
                    if char == "4":
                        ends.append(End(col * 20, row * 20, 20, 20))
        self.walls = walls
        self.enemies = enemies
        self.ends = ends

    def update(self):
        self.handle_input()
        if self.game_state == "start":
            self.render()
        if self.game_state == "game":
            self.player.move(self.walls)
            for enemy in self.enemies:
                enemy.move(self.walls)
            for exit1 in self.ends:
                if self.player.sprite.hitbox.colliderect(exit1.hitbox):
                    self.switch_level()
            self.render()
        if self.game_state == "end":
            self.render()

    def render(self):
        if self.game_state == "start":
            self.screen.fill(s.MENU_BACKGROUND_COLOR)
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect_start)
            self.screen.blit(
                self.start_text1,
                (s.WIDTH_SCREEN / 2 - self.start_text1.get_width() / 2, 200),
            )
            self.screen.blit(
                self.start_text2,
                (s.WIDTH_SCREEN / 2 - self.start_text2.get_width() / 2, 300),
            )
        if self.game_state == "game":
            self.screen.fill(s.BACKGROUND_COLOR)
            self.player.sprite.draw(self.screen)
            for wall in self.walls:
                wall.sprite.draw(self.screen)
            for enemy in self.enemies:
                enemy.sprite.draw(self.screen)
            for enemy in self.enemies:
                if self.player.sprite.hitbox.colliderect(enemy.sprite.hitbox):
                    self.won = 0
                    self.game_state = "end"
            for obj in [self.player] + self.walls + self.enemies:
                obj.sprite.draw(self.screen)
        if self.game_state == "end":
            self.screen.fill(s.MENU_BACKGROUND_COLOR)
            pygame.draw.rect(self.screen, (50, 50, 50), self.button_rect_again)
            if self.won == 1:
                self.screen.blit(
                    self.end_text1,
                    (s.WIDTH_SCREEN / 2 - self.end_text1.get_width() / 2, 200),
                )
            else:
                self.screen.blit(
                    self.end_text2,
                    (s.WIDTH_SCREEN / 2 - self.end_text2.get_width() / 2, 200),
                )
            self.screen.blit(
                self.end_text3,
                (s.WIDTH_SCREEN / 2 - self.end_text3.get_width() / 2, 300),
            )
        pygame.display.update()
        self.clock.tick(s.FPS)
