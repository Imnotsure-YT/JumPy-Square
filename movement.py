import turtle
import math
import collider
import time

screen = turtle.Screen()

fps = 120
delay = int(1000 / fps)

def updateTurtle(screen):
    screen.update()

def moveRight(turtle):
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(20)
    updateTurtle(screen)

def moveLeft(turtle):
    turtle.penup()
    turtle.setheading(0)
    turtle.backward(20)
    updateTurtle(screen)

def gravity(turtle, screen):
    counter = 0
    while turtle.ycor() > -200:
        counter += 1
        turtle.setheading(270)
        turtle.penup()
        if turtle.ycor() - (math.e * counter) / 2 < -190:
            turtle.forward(turtle.ycor() + 190)
        else:
            turtle.forward((math.e * counter) / 2)
        screen.update()
        time.sleep(0.1)

def Jump(turtle, screen):
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(100)


    gravity(turtle, screen)

def jumpRight(turtle, screen):
    Jump()
    

def jumpLeft(turtle, screen):
    pass

# movement indices: 
# 0: don't move. 1: right only. 2: left only. 3: jump. 4: jump + right. 5: jump + left. 