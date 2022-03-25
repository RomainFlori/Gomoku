from random import random
from srcs.gameManager import GameManager
from srcs.ai import AI
from srcs.utils import *
import random
import sys

# from rich import inspect, print

class Turn:
    def __init__(self, input: list, gamemanager: GameManager):
        if self.error_handling(input) != 84:
            self.runTurn(input, gamemanager)

    def runTurn(self, input, gamemanager):
        list_input = self.parseArg(input)
        # inspect(list_input)
        gamemanager._gameArea[list_input[1]][list_input[0]] = ENNEMY

        positions = AI().iaNextMove(gamemanager._gameArea)
        # print(positions)
        gamemanager._gameArea[positions[0]][positions[1]] = BRAIN
        # print(gamemanager._gameArea)

        print(f"{positions[1]},{positions[0]}")
        sys.stdout.flush()

    def parseArg(self, input):
        tmp = input[1].strip().split(",")
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
        return tmp

    def error_handling(self, input):
        if len(input) != 2:
            return 84
        tmp = input[1].strip().split(",")
        if len(tmp) != 2:
            return 84
