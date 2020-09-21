from basegame import Game


def main():
    game = Game()

    while True:

        game.events()

        if game.done:
            game.quit()
            return

        game.update()
        game.display()


if __name__ == "__main__":
    main()