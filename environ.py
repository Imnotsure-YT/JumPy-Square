import turtle

def drawGround(y, turtle, map):
    turtle.penup()
    turtle.goto(-500, y)
    turtle.pendown()
    turtle.forward(1000)
    return map
