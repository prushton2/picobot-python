from tkinter import *
import maps

def placePixel(canvas, x, y, pixeltype):
    types = {
        "empty": "white",
        "block": "blue",
        "picobot": "yellow",
        "passed": "grey"
    }
    #offset from edge of map for borders
    x += 1
    y += 1
    
    canvas.create_rectangle((x*20, y*20), (x*20+20, y*20+20), fill=types[pixeltype])

def loadMap(canvas, mapname):

    mapdata = maps.parseMap(maps.maps[mapname])
    
    limitx = 0
    limity = 0

    for i, ii in enumerate(mapdata):
        for j, jj in enumerate(mapdata[i]):
            # the list is split up so i is the i value and j is the x value. I didnt want it like this but too bad for me ig
            placePixel(canvas, j, i, mapdata[i][j])
            limity = i
            limitx = i

    print("Loaded new map")
    print(f"{limitx}; {limity}")


root = Tk()

root.geometry('500x500')
root.title('Canvas Demo')

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack(anchor=CENTER, expand=True)

# loadbtn = Button(root, text="Load", command=lambda: )

loadMap(canvas, "empty")


canvas.create_rectangle((0, 0), (500, 20), fill="blue")
canvas.create_rectangle((0, 0), (20, 500), fill="blue")
canvas.create_rectangle((500, 500), (480, 0), fill="blue")
canvas.create_rectangle((500, 500), (0, 480), fill="blue")


root.mainloop()