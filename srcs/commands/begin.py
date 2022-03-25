from random import random
from srcs.gameManager import GameManager
from srcs.utils import *
import random
import sys

class Begin:
    def __init__(self, input: list, gameManager: GameManager):
        if (self.errorHandling(input) != 84) :
            self.runBegin(input, gameManager)

    def errorHandling(self, input):
        if len(input) != 1:
            print('ERROR - No argument needed.')
            return 84

        return 0

    def runBegin(self, input, gameManager):

        # gameManager._gameArea[list_input[0]][list_input[1]] = ENNEMY
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        gameManager._gameArea[x][y] = BRAIN
        print(f'{y},{x}')
        sys.stdout.flush()
