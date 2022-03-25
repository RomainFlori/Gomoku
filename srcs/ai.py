##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## ai
##
#from asyncio.windows_events import NULL
from srcs.utils import *
from srcs.gameManager import GameManager
from srcs.moves import *
import random

# from rich import inspect, print

all_patterns = [ "0XXXX", "X0XXX", "XX0XX", "XXX0X", "XXXX0", 
                "0OOOO", "O0OOO", "OO0OO", "OOO0O", "OOOO0",
                "0OOO", "O0OO", "OO0O", "OOO0",
                "0XXX", "X0XX", "XX0X", "XXX0",
                "X0", "0X" ]

all_counter_pat = [ "0OOOO", "O0OOO", "OO0OO", "OOO0O", "OOOO0", "0OOO", "O0OO", "OO0O", "OOO0" ]

class AI:
    def iaNextMove(self, gameManager):
        # inspect(gameManager)
        # firstmove_pos = self.firstMove(gameManager)
        # if firstmove_pos != False :
        #     return firstmove_pos
        # else :
        positions = self.iaMoving(gameManager)
        if positions != None:
            return positions
        else:
            return self.randomMove(gameManager)

    def iaMoving(self, gameManager):
        for pattern in all_patterns:
            # print("le pattern :")
            # print(pattern)
            for y in range(len(gameManager)):
                for x in range(len(gameManager)):
                    if gameManager[y][x] == "O":
                        counter_positions = self.testAllMoves(gameManager, y, x, pattern)
                        if counter_positions != None: return counter_positions

                    if gameManager[y][x] == "X":
                        positions = self.testAllMoves(gameManager, y, x, pattern)
                        if positions != None: return positions

        return None

    def testAllMoves(self, gameManager, y, x, pattern):
        positions = horizontalMove(gameManager, y, x, pattern)
        if positions != None: return positions

        positions = verticalMove(gameManager, y, x, pattern)
        if positions != None: return positions

        positions = diagonaleRightMove(gameManager, y, x, pattern)
        if positions != None: return positions

        positions = diagonaleLeftMove(gameManager, y, x, pattern)
        if positions != None: return positions

        return None


    def randomMove(self, gameManager):
        y = random.randint(0, 19)
        x = random.randint(0, 19)

        if self.checkIfTakken(gameManager, y, x):
            while self.checkIfTakken(gameManager, y, x) == True:
                y = random.randint(0, 19)
                x = random.randint(0, 19)
        return [y, x]

    def firstMove(self, gameManager):
        for line in gameManager:
            if BRAIN in line:
                return False

        totalLen = len(gameManager)
        middle = int((totalLen / 2) - 1)
        if self.checkIfTakken(gameManager, middle, middle):
            return (middle + 1, middle)
        else:
            return (middle, middle)

    def checkIfTakken(self, gameBoard, y, x):
        if gameBoard[y][x] == 0:
            return False
        return True
