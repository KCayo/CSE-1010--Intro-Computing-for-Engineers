# Monte Carlo Simulation
# CSE1010 Homework 4, Fall 2018
# Kevin Cayo
# 9/26/2018
# TA: Nila Mandel
# Lab section: 015L
# Instructor: Ahmad Jbara

import math
import random
import tkinter

# dimensions of the field
FIELD_W = 600
FIELD_H = 600

# position and size of the pond
POND_X = 300
POND_Y = 300
POND_R = 150

# number of shots to fire
NUM_SHOTS = 1000

def drawCircle(canvas, x, y, r, outline='black', fill='white'):
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=outline)

def drawPond(canvas):
    drawCircle(canvas, POND_X, POND_Y, POND_R, 'blue4', 'DodgerBlue3')

def drawField(canvas):
    drawCircle(canvas, POND_X, POND_Y, 1000, 'forest green', 'forest green')


def hitPond(x,y):
    distance = ((POND_X-x)**2)+((POND_Y-y)**2)**(1/2)
    if distance>POND_R:
        return 'False'
    elif distance<=POND_R:
        return 'True'

def plotShot(canvas,x,y):
    if hitPond(x,y)=='True':
        drawCircle(canvas, x, y, 5, outline='medium blue',fill='medium blue')
        return True
    elif hitPond(x,y)=='False':
        drawCircle(canvas, x, y, 5, outline='dark green', fill='dark green')
        return False

def fireShot(canvas, shots):
    pancake=0
    splashes=0
    while pancake<=shots:
        xshot=random.randint(0,FIELD_W)
        yshot=random.randint(0,FIELD_H)
        plotShot(canvas, xshot, yshot)
        pancake=pancake+1
        if hitPond(xshot, yshot)=='True':
            splashes=splashes+1
    return splashes

def estimatePondArea (splashes, num):
    area=FIELD_W*FIELD_H
    ratio=splashes/num
    pondarea=area*ratio
    return pondarea
    
def initWindow(title, width, height):
    master = tkinter.Tk()
    master.title(title)
    canvas = tkinter.Canvas(master, width=width, height=height)
    canvas.pack()
    return canvas

def main():
    canvas = initWindow("Monte Carlo Simunlation", FIELD_W, FIELD_H)
    drawField(canvas)
    drawPond(canvas)
    numSplashes=fireShot(canvas, NUM_SHOTS)
    estPondArea = estimatePondArea(numSplashes, NUM_SHOTS)
    estPondArea = round(estPondArea, 1)
    print("Estimated pond area:", estPondArea)
    actPondArea = round(math.pi * POND_R**2, 1)
    print("Actual pond area:", actPondArea)
    err = round(abs(actPondArea-estPondArea) / actPondArea * 100, 1)
    print("Error:", err, "%")
    print('Number of shots: ', NUM_SHOTS)
    print('Number of splashes: ', numSplashes)

    
if __name__ == '__main__':
    main()
    tkinter.mainloop()
    
