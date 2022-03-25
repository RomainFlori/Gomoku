import sys
from srcs.gameManager import GameManager
from srcs.commands.start import Start
from srcs.commands.end import End
from srcs.commands.turn import Turn
from srcs.commands.begin import Begin
from srcs.commands.info import Info
from srcs.commands.about import About
from srcs.commands.board import Board

# from rich import inspect, print


COMMANDS = ["START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT"]
FUNCTIONS_STR = [
    "startCmd",
    "turnCmd",
    "beginCmd",
    "boardCmd",
    "infoCmd",
    "endCmd",
    "aboutCmd",
]


class Game:
    def __init__(self):
        self._commands = {
            "START": Start,
            "END": End,
            "TURN": Turn,
            "BEGIN": Begin,
            "INFO": Info,
            'ABOUT': About,
            'BOARD': Board,
        }
        self._gameManager = GameManager()

    def loop(self):
        while 1:
            lineinput = sys.stdin.readline()
            InputsCommands = lineinput.strip().split(" ")
            if InputsCommands[0] in COMMANDS:
                self._commands[InputsCommands[0]](InputsCommands, self._gameManager)
            else:
                print('ERROR unknown command "{}"'.format(InputsCommands[0]))


if __name__ == "__main__":
    foo = Game()
    foo.loop()
