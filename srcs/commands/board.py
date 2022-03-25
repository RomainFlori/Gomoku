from random import random
from srcs.gameManager import GameManager
from srcs.ai import AI
from srcs.utils import *
import random
import sys

# from rich import inspect, print


class Board:
    def __init__(self, input: list, gameManager: GameManager):
        if (self.errorHandling(input) != 84) :
            self.runBoard(input, gameManager)

    def errorHandling(self, input):
        if len(input) != 1:
            print('ERROR - No argument needed.')
            return 84

        return 0

    def runBoard(self, input, gameManager):
        while True :
            lineinput = sys.stdin.readline()
            InputsCommands = lineinput.strip().split(",")
            if ((InputsCommands[0] == "DONE")):
                break
            if (len(InputsCommands) < 3):
                print("ERROR - Invalid command")
                return 84
            if (InputsCommands[2] == '1'):
                tmp = BRAIN
            elif (InputsCommands[2] == '2'):
                tmp = ENNEMY
            elif (InputsCommands[2] == '3'):
                tmp = 3
            else :
                print("ERROR - Invalid command")
                return 84
            gameManager._gameArea[int(InputsCommands[1])][int(InputsCommands[0])] = (tmp)

        positions = AI().iaNextMove(gameManager._gameArea)
        # print(positions)
        gameManager._gameArea[positions[0]][positions[1]] = BRAIN

        print(f"{positions[1]},{positions[0]}")
        sys.stdout.flush()
        # print(gameManager._gameArea)
