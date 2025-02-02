from game_manager import GameManager


def main():
    gm = GameManager()

    while True:
        gm.update()

if __name__ == "__main__":
    main()
