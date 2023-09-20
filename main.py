from tkinter import *
import tkinter as tk
import random
import time

import canvasManager as cm
import maps

import script
import picobot

global canvas
canvas = None




#This code runs the users code

def run():
    print(picobot.stateFunctions)
    while(picobot.cstate != -1):
        picobot.stateFunctions[picobot.cstate]()
        canvas.update()
        time.sleep(0.01)




root = Tk()

root.geometry('700x500')
root.title('Canvas Demo')
#Frames

canvasFrame = Frame(root)
cpanelFrame = Frame(root)
navFrame = Frame(cpanelFrame)
controlFrame = Frame(cpanelFrame)

#Elements
canvas = Canvas(canvasFrame, width=500, height=500, bg='white')
resetbtn = Button(controlFrame, text="Reset Picobot", command=lambda: picobot.reset())
runbtn = Button(controlFrame, text="Run", command=lambda: run())
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

#Other functions
cm.loadMap(canvas, "empty")

picobot.load(canvas)


root.mainloop()