from tkinter import *
import tkinter as tk
import random
import time

import canvasManager as cm
import maps

import script
import picobot

canvas = None
currentMapIndex = 0
maplabel = None


#This code runs the users code

def run():
    print(picobot.stateFunctions)
    while(picobot.cstate != -1):
        picobot.stateFunctions[picobot.cstate]()
        canvas.update()
        time.sleep(0.01)


def chgMap(i):
    global currentMapIndex
    global maplabel

    currentMapIndex += i
    currentMapIndex %= len(maps.maps)
    cm.loadMap(canvas, list(maps.maps)[currentMapIndex])

    maplabel.config(text=list(maps.maps.keys())[currentMapIndex])


root = Tk()

root.geometry('700x500')
root.title('Canvas Demo')
#Frames

canvasFrame = Frame(root)
cpanelFrame = Frame(root)
navFrame = Frame(cpanelFrame)
controlFrame = Frame(cpanelFrame)
mapFrame = Frame(cpanelFrame)

#Elements
canvas = Canvas(canvasFrame, width=500, height=500, bg='white')

resetbtn = Button(controlFrame, text="Reset Picobot", command=lambda: picobot.reset())
runbtn = Button(controlFrame, text="Run", command=lambda: run())

mapleft  = Button(mapFrame, text="<<", command=lambda: chgMap(-1))
maplabel = Label (mapFrame, text="Empty")
mapright = Button(mapFrame, text=">>", command=lambda: chgMap(1))

N = Button(navFrame, text="N", command=lambda: picobot.move("N"))
E = Button(navFrame, text="E", command=lambda: picobot.move("E"))
W = Button(navFrame, text="W", command=lambda: picobot.move("W"))
S = Button(navFrame, text="S", command=lambda: picobot.move("S"))

#Grid
canvasFrame.grid(row=0,column=0)
canvas.grid(row=0,column=0)

cpanelFrame.grid(row=0,column=1)

controlFrame.grid(row=0,column=0)
resetbtn.grid(row=0,column=0)
runbtn.grid(row=0,column=2)

navFrame.grid(row=1,column=0)
N.grid(row=0,column=1)
E.grid(row=1,column=3)
W.grid(row=1,column=0)
S.grid(row=1,column=1)

mapFrame.grid(row=2,column=0)
mapleft.grid(row=0,column=0)
maplabel.grid(row=0,column=1)
mapright.grid(row=0,column=2)

#Other functions
cm.loadMap(canvas, list(maps.maps)[currentMapIndex])

picobot.load(canvas)


root.mainloop()