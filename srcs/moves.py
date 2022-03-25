##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## moves
##

# from rich import inspect, print

def horizontalMove(gameManager, y, x, pattern):
    pos = None
    for i in range(x, x + len(pattern)):
        if i > (len(gameManager) - 1) or str(gameManager[y][i]) != (pattern[i - x]):
            pos = None
            # print("str(gameManager[y])", str(gameManager[y]), " et :", str(gameManager[y][i]))
            # print("(pattern[i - x])", (pattern[i - x]))
            break
        elif pattern[i - x] == "0":
            # print("un bon pattern :")
            pos = [y, i]
            # return [y, i]
    if pos == None :
        pos = invertHorizontalMove(gameManager, y, x, pattern)

    return pos

def invertHorizontalMove(gameManager, y, x, pattern):
    i = 0
    pos = None

    for i in range(x, x - len(pattern), -1):
        if i < 0 or str(gameManager[y][i]) != (pattern[-(i - x)]):
            pos = None
            break
        elif pattern[-(i - x)] == "0":
            # return [y, i]
            pos = [y, i]
    return pos

def verticalMove(gameManager, y, x, pattern):
    pos = None

    for i in range(y, y + len(pattern)):
        if i > (len(gameManager) - 1) or str(gameManager[i][x]) != (pattern[i - y]):
            pos = None
            break
        elif pattern[i - y] == "0":
            # return [i, x]
            pos = [i, x]
    if pos == None :
        pos = invertVerticalMove(gameManager, y, x, pattern)

    return pos

def invertVerticalMove(gameManager, y, x, pattern):
    i = 0
    pos = None
    for i in range(y, y - len(pattern), -1):
        if i < 0 or str(gameManager[i][x]) != (pattern[-(i - y)]):
            pos = None
            break
        elif pattern[-(i - y)] == "0":
            pos = [i, x]
            # return [i, x]
    return pos

def diagonaleRightMove(gameManager, y, x, pattern):
    pos = None
    the_y = 0

    for i in range(x, x + len(pattern)):
        if (y + the_y) > (len(gameManager) - 1) or (x + the_y) > (len(gameManager) - 1):
            pos = None
            break
        # print('gameManager[y :', gameManager[y])

        if str(gameManager[y + the_y][x + the_y]) != (pattern[the_y]):
            pos = None
            break
        if pattern[the_y] == "0":
            pos = [y + the_y, x + the_y]
        the_y += 1

    if pos == None :
        pos = invertDiagonaleRightMove(gameManager, y, x, pattern)

    return pos

def invertDiagonaleRightMove(gameManager, y, x, pattern):
    the_y = 0
    pos = None

    for i in range(x, x + len(pattern)):
        if (y - the_y) < 0 or (x - the_y) < 0 :
            pos = None
            break

        if str(gameManager[(y - the_y)][(x - the_y)]) != (pattern[the_y]):
            # print("gameManager[-(y - the_y)] :", gameManager[(y - the_y)][(x - the_y)])
            # print("(pattern[-the_y]) :", (pattern[the_y]))
            pos = None
            break

        elif pattern[the_y] == "0":
            # print('je suis le 0')
            # print("le y :", the_y)
            pos = [y - the_y, x - the_y]

        the_y += 1
    return pos


def diagonaleLeftMove(gameManager, y, x, pattern):
    pos = None
    the_y = 0
    for i in range(x, x + len(pattern)):
        if (y + the_y) > (len(gameManager) - 1) or (x - the_y) < 0:
            pos = None
            break
        if str(gameManager[y + the_y][x - the_y]) != (pattern[the_y]):
            pos = None
            break
        if pattern[the_y] == "0":
            pos = [y + the_y, x - the_y]
        the_y += 1

    if pos == None :
        pos = invertDiagonaleLeftMove(gameManager, y, x, pattern)

    return pos

def invertDiagonaleLeftMove(gameManager, y, x, pattern):
    the_y = 0
    pos = None

    for i in range(x, x + len(pattern)):
        if (y - the_y) < 0 or (x + the_y) > (len(gameManager) - 1) :
            pos = None
            break

        if str(gameManager[(y - the_y)][(x + the_y)]) != (pattern[the_y]):
            pos = None
            break

        elif pattern[the_y] == "0":
            pos = [y - the_y, x + the_y]

        the_y += 1
    return pos