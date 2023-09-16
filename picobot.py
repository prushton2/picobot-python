picobot = [-1, -1]

def ResetPicoBot(canvas):

    placePixel(canvas, picobot[0], picobot[1], "empty")
    choice = None
    x = 0
    y = 0
    while(choice != "empty"):
        x = random.randint(0, 22)
        y = random.randint(0, 22)
        choice = loadedMap[y][x]

    picobot = [x, y]
    placePixel(canvas, x, y, "picobot")
