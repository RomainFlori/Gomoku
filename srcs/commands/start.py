# from rich import inspect
from typing import List
from srcs.gameManager import GameManager
import sys

class Start:
    def __init__(self, input: List[str], gameManager: GameManager):
        if self.error_handling(input) != 84:
            self.start_run()

    def error_handling(self, input: list):
        if len(input) != 2:
            print("ERROR message - unsupported size or other error", end="")
            return 84
        if int(input[1]) < 5:
            print("ERROR message - unsupported size or other error", end="")
            sys.exit(84)
            return 84
        if int(input[1]) > 100:
            print("ERROR message - unsupported size or other error", end="")
            sys.exit(84)
            return 84
        # if (input[1].isalpha()):
        #     print("ERROR message - enter a number")
        #     return 84
        return 0

    def start_run(self):
        print("OK")
        sys.stdout.flush()

    # def IsAInt(self, input):
    #     try:
    #         int(input[1])
    #     except ValueError:
    #         return False
    #     else:
    #         return True
