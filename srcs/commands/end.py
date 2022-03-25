import sys
from srcs.gameManager import GameManager


class End:
    def __init__(self, InputList: list, gameManager: GameManager):
        self.exit()

    def exit(self):
        sys.exit(0)
