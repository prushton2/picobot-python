import canvasManager as cm
import random

picobot = [-1, -1]
tkCanvas = None
cstate = 0
stateFunctions = {}

def load(canvas):
    global tkCanvas
    tkCanvas = canvas

def reset():

    global picobot
    global tkCanvas
    if(picobot != [-1, -1]):
        cm.placePixel(tkCanvas, picobot[0], picobot[1], "empty")
    choice = None
    x = 0
    y = 0
    while(choice != "empty"):
        x = random.randint(0, 22)
        y = random.randint(0, 22)
        choice = cm.loadedMap[y][x]

    picobot = [x, y]
    cm.placePixel(tkCanvas, x, y, "picobot")


def move(dir):
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

    cm.placePixel(tkCanvas, picobot[0], picobot[1], "passed")

    picobot = newPos

    cm.placePixel(tkCanvas, picobot[0], picobot[1], "picobot")

def get(sides):

    sideStates = [
        cm.loadedMap[picobot[1]-1][picobot[0]] == "block",
        cm.loadedMap[picobot[1]][picobot[0]+1] == "block",
        cm.loadedMap[picobot[1]][picobot[0]-1] == "block",
        cm.loadedMap[picobot[1]+1][picobot[0]] == "block"
    ]


    for i, e in enumerate(sides):
        if(e == "*"):
            continue

        if(e == "x" and sideStates[i]):
            return False
        
        if(e in ["N", "E", "W", "S"] and not sideStates[i]):
            return False
        
    return True



def setstate(newState):
    global cstate
    cstate = newState


def state(state):
    def wrap(fn):
        global stateFunctions
        stateFunctions[state] = fn
    return wrap

