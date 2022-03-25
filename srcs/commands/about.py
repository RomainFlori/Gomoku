import sys
from srcs.gameManager import GameManager

ABOUT = 'name="IAROM1", version="0.1", author="romain.flori-cantrelle@epitech.eu", country="France"'


class About:
    def __init__(self, InputList: list, gameManager: GameManager):
        self.about()

    def about(self):
        print(ABOUT)
        sys.stdout.flush()