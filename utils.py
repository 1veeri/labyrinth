# from wall import Wall
# from enemy import Enemy
# from player import Player
# from exit import End



# def load_level(level_number, walls, enemies, ends):
#     walls.clear()
#     enemies.clear()
#     ends.clear()
#     with open(rf"assets\levels\lvl{level_number}.txt") as level:
#         for row, line in enumerate(level.read().splitlines()):
#             for col, char in enumerate(line):
#                 if char == "1":
#                     walls.append(
#                         Wall(col * 20, row * 20, 20, 20, r"assets\images\wall.png")
#                     )
#                 if char == "2": 
#                     enemies.append(
#                         Enemy(col * 20, row * 20, 20, 20, r"assets\images\enemy.png", 5)
#                     )
#                 if char == "3":
#                         player = Player(col * 20, row * 20, 20, 20, r"assets\images\player.png", 5)
#                 if char == "4":
#                     ends.append(
#                          End(col * 20, row * 20, 20, 20)
#                     )
#     return player
    