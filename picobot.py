import canvasManager as cm
import random

picobot = [-1, -1]

def reset(canvas):

    global picobot
    if(picobot != [-1, -1]):
        cm.placePixel(canvas, picobot[0], picobot[1], "empty")
    choice = None
    x = 0
    y = 0
    while(choice != "empty"):
        x = random.randint(0, 22)
        y = random.randint(0, 22)
        choice = cm.loadedMap[y][x]

    picobot = [x, y]
    cm.placePixel(canvas, x, y, "picobot")


def move(canvas, dir):
    global picobot
    newPos = []

    dirmap = {
        "N": [0, -1],
        "E": [1, 0],
        "W": [-1, 0],
        "S": [0, 1]
    }

    newPos = [picobot[0] + dirmap[dir][0], picobot[1] + dirmap[dir][1]]

    if(cm.loadedMap[newPos[1]][newPos[0]] != "empty"):
        return

    cm.placePixel(canvas, picobot[0], picobot[1], "passed")

    picobot = newPos

    cm.placePixel(canvas, picobot[0], picobot[1], "picobot")


stateFunctions = {}


def state(state):
    def wrap(fn):
        global stateFunctions
        stateFunctions[state] = fn
    return wrap

