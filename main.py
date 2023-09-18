from tkinter import *
import maps
import random
import picobot
import canvasManager as cm


root = Tk()

root.geometry('500x700')
root.title('Canvas Demo')

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack(anchor=CENTER, expand=True)

randbtn = Button(root, text="Load", command=lambda: picobot.reset(canvas))
randbtn.pack()


N = Button(root, text="N", command=lambda: picobot.move(canvas, "N"))
E = Button(root, text="E", command=lambda: picobot.move(canvas, "E"))
W = Button(root, text="W", command=lambda: picobot.move(canvas, "W"))
S = Button(root, text="S", command=lambda: picobot.move(canvas, "S"))

N.pack()
E.pack()
W.pack()
S.pack()

cm.loadMap(canvas, "testmap")


canvas.create_rectangle((0, 0), (500, 20), fill="blue")
canvas.create_rectangle((0, 0), (20, 500), fill="blue")
canvas.create_rectangle((500, 500), (480, 0), fill="blue")
canvas.create_rectangle((500, 500), (0, 480), fill="blue")


root.mainloop()