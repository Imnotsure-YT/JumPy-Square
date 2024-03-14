import turtle
import time
import environ
import movement

mvtIndex = 0

turtle.tracer(0)
screen = turtle.Screen()

def setUp(col):
    setUp = turtle.Turtle()
    turtle.screensize(1000, 500)
    environ.drawGround(-200, setUp, col)

    return col

fps = 120
delay = int(1000 / fps)

def updateTurtle(screen):
    screen.update()  

def drawPlayer (turtle):
    turtle.color("red")
    turtle.shape("square")

def main():
    colliders = []
    player1 = turtle.Turtle()
    drawPlayer(player1)
    colliders = setUp(colliders)
    player1.penup()
    player1.goto(0, 200)
    player1.pendown()

    screen.listen()
    screen.onkeypress(lambda: movement.Jump(player1, screen), "space")
    screen.onkeypress(lambda: movement.moveLeft(player1), "a")
    screen.onkeypress(lambda: movement.moveRight(player1), "d")

    while player1.ycor() > -200:
        movement.gravity(player1, screen)

main()

turtle.exitonclick()