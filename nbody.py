# N-Body Simulation
# CSE1010 Homework 5, Fall 2018
# Kevin Cayo
# 10/06/18
# TA: Nila Mandel
# Lab section: 015L
# Instructor: Ahmad Jbara

import math, random, time, turtle

NBodies = 10
G = 10
SpaceRadius = 250
MinMass = 5
MaxMass = 100
MaxVelocity = 100
BodyColor = 'black'
TraceColor = 'green'

turtles = []
masses = []
Xs = []
Ys = []
Vxs = []
Vys = []

OffScreen = []
WinX2 = 0
WinY2 = 0

def newTurtle():
 a = turtle.Turtle()
 turtles.append(a)
 a.speed(0)
 a.pensize(5)
 return a

def printBodyInfo(n):
    print('Body', n, 'mass =', masses[n], ', x =', Xs[n], ', y =',
         Ys[n], ', vx =', Vxs[n], ', vy =', Vys[n])

def initBody(t):
    b = random.randint(MinMass,MaxMass)
    masses.append(b)
    t.turtlesize(b * 0.03, b * 0.03, 0)
    t.shape('circle')
    x_location = random.randint(-SpaceRadius,SpaceRadius)
    Xs.append(x_location)
    y_location = random.randint(-SpaceRadius,SpaceRadius)
    Ys.append(y_location)
    x_velocity = random.randint(-MaxVelocity,MaxVelocity)/100
    Vxs.append(x_velocity)
    y_velocity = random.randint(-MaxVelocity,MaxVelocity)/100
    Vys.append(y_velocity)
    OffScreen.append(False)
    t.penup()
    t.goto(x_location,y_location)
    t.pendown()

def setup():
    turtle.tracer(0,0)
    for c in range(NBodies):
        t = newTurtle()
        initBody(t)
        printBodyInfo(c)
    turtle.update()

def moveBody(e):
    x_new = Xs[e] + Vxs[e]
    Xs[e] = x_new
    y_new = Ys[e] + Vys[e]
    Ys[e] = y_new
    t = turtles[e]
    t.hideturtle()
    t.pencolor(TraceColor)
    t.goto(x_new,y_new)
    t.pencolor(BodyColor)
    t.showturtle()
    if x_new < -WinX2 or x_new > WinX2 or y_new < -WinY2 or y_new > WinY2:
        OffScreen[e] = True

def moveBodies():
    for e in range(NBodies):
        t = turtles[e]
        if t is not None:
            moveBody(e)

def calculateForce(body1, body2):
    m1 = masses[body1]
    m2 = masses[body2]
    x1 = Xs[body1]
    y1 = Ys[body1]
    x2 = Xs[body2]
    y2 = Ys[body2]
    dx = x2 - x1
    dy = y2 - y1
    r = math.sqrt(((dx)**2)+((dy)**2))
    f = G*((m1*m2)/(r**2))
    angle_force = math.atan2(dy,dx)
    fx = f * math.cos(angle_force)
    fy = f * math.sin(angle_force)
    return fx, fy

def accelerateBody(g):
    for h in range(NBodies):
        if h != g:
            fx, fy = calculateForce(g,h)
            x_acceleration = fx / masses[g]
            y_acceleration = fy / masses[g]
            x_accelocity = x_acceleration + Vxs[g]
            Vxs[g] = (x_accelocity)
            y_accelocity = y_acceleration + Vys[g]
            Vys[g] = (y_accelocity)

def accelerateBodies():
    for i in range(NBodies):
        t = turtles[i]
        if t is not None:
            accelerateBody(i)

def main():
    print('N-Body simulation starting')
    screen = turtle.Screen()
    screen.title('N-Body Simulator')
    global WinX2, WinY2
    WinX2 = screen.window_width() / 2
    WinY2 = screen.window_height() / 2
    setup()
    while not all(OffScreen):
        moveBodies()
        accelerateBodies()
        turtle.update()
    print('Program finished')
    screen.mainloop()

if __name__ == '__main__':
 main()
